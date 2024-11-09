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


def validate_data(values):
    """
    This try converts all string values to int.
    pops up ValueError when its impossible, or if
    more than 4 values appear.
    """
    try:
        if len(values) != 4:
            raise ValueError(f"4 value needed, you provided is {len(values)}"

            )
    except ValueError is e:
        print(f"invalid data: {e}, please try again!\n")



    print(values)

def get_players_data():
    """
    get players info from the available data
    """
    print("Enter the players data on monday.")
    print("Data should be four numbers separated by commas.")
    print("Example: 10,20,30,40\n")

data_str = input("Enter your data here: ")

players_data = data_str.split(",")
validate_data(players_data)


get_players_data()


