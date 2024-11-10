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


 # Get players' info from the available data.    
def get_players_data():
    
    players = SHEET.worksheet('players').get_all_values()[-7:]
    #converting strings to integers
    return [[int(num)for num in row] for row in players]


def get_games_data():

    games = SHEET.worksheet('games').get_all_values()[-7:]
    #converting strings to integers
    return [[int(num)for num in row] for row in games]


def calculating_max_totals(players_data, games_data):
    """
    cal maximum amount of studio players per day and for a week
    cal maximum amount of games per day and for a week

    """
    #total for players in a day an week

    max_players_per_day = [max(day) for day in players_data]

    max_games_per_day = [max(day) for day in games_data]


    #totals for games in a day and a week

    total_max_player_week = sum(max_players_per_day)

    total_max_games_week = sum(max_games_per_day)

    print(f"Maximum players per in a week: {max_players_per_day}")
    print(f"maximum games per day: {max_games_per_day}")
    print(f"total max game week: {total_max_games_week}")
    print(f"total maximum players week: {total_max_player_week}") 


    return max_players_per_day, max_games_per_day, total_max_player_week, total_max_games_week

    #calculate average game time and rewards
def calculate_daily_statistics(max_games_per_day, max_players_per_day):
    hours_per_day = 5
    total_minutes = hours_per_day * 60


    for i, games in enumerate(max_game_per_day):
        if games > 0:
            avg_game_time = total_minutes / games #average time per game
        else:
            avg_game_time = 0 

        muffins_per_person = max_players_per_day[i] # 1 muffin per person
        daily_rewards = games * 10   # 10 per game won

        print(f"Day {i+1}:")
        print(f"  Average game time: {avg_game_time:.2f} minutes")
        print(f"  Muffins given: {muffins_per_day}")
        print(f"  Total dollars awarded: ${daily_rewards}")

# Execute the calculations
games_data = get_games_data()
players_data = get_players_data()

max_players_per_day, max_games_per_day, total_max_players_week, total_max_games_week = calculating_max_totals(players_data, games_data)

calculate_daily_statistics(max_games_per_day, max_players_per_day)
    


        



    


    