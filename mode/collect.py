import questionary

from collector.source import find_from_keyword
from rich import print

def collect():

    while True:
        # Ask for user keyword, then search it up
        keyword = questionary.text("What would you like to search?").ask()

        if keyword is None:
            break

        if keyword:
            # This function returns number of news that was inserted into the db

            print("Please wait...")

            parsed = find_from_keyword(keyword)

            print(f"Found: {parsed[0]}")
            print(f"Parsed: {parsed[1]}")
            print(f"Inserted: {parsed[2]}")
            print(f"Skipped or already stored: {parsed[1] - parsed[2]}")

            break
        else:
            print("Please enter keyword")