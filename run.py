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
def get_players_week_data():
    
    players = SHEET.worksheet('players')

    data = players.get_all_values().get_all_values()[-7:]
    #converting strings to integers
    return [int[(num)for num in row] for num in players]


def get_games_data():
    games = SHEET.worksheet('players')

    data = games.get_all_values().get_all_values()[-7:]
    #converting strings to integers
    return [int[(num)for num in row] for num in games]


    """
    while True:
        print("maximum players per day:", max_players_per_day)
        print("max game per day (assumimg 12min per game):", max_game_per_day)
        print("total maximum players in

        # Prompt the user for input
        data_str =

    return players_data

    

def validate_data(values):
    
    Convert all string values to integers. Raises a ValueError if conversion fails or if more than 4 values are provided.
    
    try:
        # Convert values to integers

        [int(value) for value in values]
        if len(values) != 4:
            raise ValueError(
                f"4 values are needed; you provided {len(values)}."
            )
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again!\n")
        return False

    return True
"""
# Call the function to get the data
#get_players_data()


    """
    Get games info from the data
    
     games = SHEET.worksheet('games')
    data = games.get_all_values()

    print(data)  # Display games data
    return data
   """

def calculate max totals(players_data, games_data):
    """
    cal maximum amount of studio players per day and for a week
    cal maximum amount of games per day and for a week

    """
    #total for players in a day an week

    max_players_per_day =[max(day) for day in players_data]

    max_games_per_day = [max(day) for day in games_data]


    #totals for games in a day and a week

    total_max_player_per_day = sum(max_players_per_day)

    total_max_games_week = sum(max_games_per_day)

    print(f"Maximum players per in a week:", max_players_per_day)
    print(f"maximum games per day:", max_games_per_day)
    print(f"total max game per week:", total_max_games_per_day)
    print(f"total maximum players per week:", total_max_player_per_day) 

    
    return max_players_week


    #fetch game data and cal maximum game played in a week
players_data = get_players_data()
max_studio_players(players_data)



def max_studio_games(games_data):
    
   # cal maximum amount of sudio games per day and 
    #maximum for a week
    
    total_games_per_day = [max(map(int, day)) for day in games_data]

    max_games_week = sum(total_games_per_day)

    print(f"Maximum games played in a week: {max_games_week}")
    return max_games_week

    #fetch game data and cal maximum game played in a week
games_data = get_games_data()
max_studio_games(games_data)


def daily_rewards():
