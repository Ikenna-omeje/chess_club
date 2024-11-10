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

players = SHEET.worksheet('players')
data = players.get_all_values()



    
def get_players_data():
    """
    Get players' info from the available data, looping until valid data is provided.
    """
    while True:
        print("Enter the players' data for Monday.")
        print("Data should be four numbers separated by commas.")
        print("Example: 10,20,30,40\n")

        # Prompt the user for input
        data_str = input("Enter your data here: ")

        # Split the input string by commas to get individual values     
        players_data = data_str.split(",")

        # Validate the data
        if validate_data(players_data):
            print("Data is valid!")
            break  # Exit the loop once data is valid

    return players_data

def validate_data(values):
    """
    Convert all string values to integers. Raises a ValueError if conversion fails or if more than 4 values are provided.
    """
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

# Call the function to get the data
get_players_data()

def get_games_data():
    """
    Get games info from the data
    """
    games = SHEET.worksheet('games')
    data = games.get_all_values()

    print(data)  # Display games data
    return data

def max_studio_players(players_data):
    """
    cal maximum amount of studio players per day and 
    maximum for a week
    """
    players = SHEET.worksheet('players').get_all_values()
    players_row = players[-7]
    print(players_row)
    
    total_players_per_day = [max(map(int, day)) for day in players_data]

    max_players_week = sum(total_players_per_day)

    print(f"Maximum players visiting in a week: {max_players_week}")
    
    return max_players_week

    #fetch game data and cal maximum game played in a week
players_data = get_players_data()
max_studio_players(players_data)

"""
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
"""



