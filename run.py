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
    get players info from the available data
    """
    print("Enter the players data on monday.")
    print("Data should be four numbers separated by commas.")
    print("Example: 10,20,30,40")

data_str = input("enter your data here: ")
print(f"the data entered is {data_str}")

get_players_data()

