import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('chess_club')


"""
fetch players and number of games info from the available chess-club data.
"""


def get_players_data():
    players = SHEET.worksheet('players').get_all_values()[-7:]
    # converting strings to integers
    return [[int(num)for num in row] for row in players]


def get_games_data():

    games = SHEET.worksheet('games').get_all_values()[-7:]
    # converting strings to integers
    return [[int(num)for num in row] for row in games]


def input_new_data():
    """
    Allows new user to enter new player and game
    data for one day.
    """
    print("Enter players'and game data for a single day.")
    print("Data should be four numbers separated by commas.")
    print("Example: 10,20,30,40\n")

    # input single player data
    player_data_input = input("enter player data here: ")
    player_data = [int(num) for num in player_data_input.split(',')]

    # input single games data
    game_data_input = input("enter game data here: ")
    game_data = [int(num) for num in game_data_input.split(',')]

    return [player_data], [game_data]


def calculating_max_totals(players_data, games_data):
    """
    cal maximum amount of studio players per day and for a week
    cal maximum amount of games per day and for a week
    """
    # total for players in a day an week

    players_day = [max(day) for day in players_data]
    games_day = [max(day) for day in games_data]

    # totals for games in a day and a week
    t_players_week = sum(players_day)
    t_games_week = sum(games_day)

    print(f"Maximum players per in a week: {players_day}")
    print(f"maximum games per day: {games_day}")
    print(f"total max game week: {t_games_week}")
    print(f"total maximum players week: {t_players_week}")

    return players_day, games_day, t_players_week, t_games_week


# calculate average game time and rewards
def calculate_daily_statistics(games_day, players_day):
    hours_per_day = 5
    total_minutes = hours_per_day * 60

    for i, games in enumerate(games_day):
        if games > 0:
            avg_game_time = total_minutes/games  # average time per game
        else:
            avg_game_time = 0

        muffins_per_person = players_day[i]  # 1 muffin per person
        daily_rewards = games * 10   # 10 per game won

        print(f"Day {i+1}:")
        print(f"Average game time: {round(avg_game_time)} minutes")
        print(f"Muffins given: {muffins_per_person}")
        print(f"Total dollars awarded: ${daily_rewards}")


# Execute the calculations
new_data_choice = input(
    "Would you like to input new data? (yes/no): ").strip().lower()

if new_data_choice == "yes":
    players_data, games_data = input_new_data()
else:
    games_data = get_games_data()
    players_data = get_players_data()

players_day, games_day, t_players_week, t_games_week = calculating_max_totals(
    players_data, games_data)
calculate_daily_statistics(games_day, players_day)
    


        



    


    