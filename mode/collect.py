import questionary

from collector.source import find_from_keyword

def collect():

    while True:
        # Ask for user keyword, then search it up
        keyword = questionary.text("What would you like to search?").ask()

        if keyword is None:
            break

        if keyword:
            # This function returns number of news that was inserted into the db
            inserted = find_from_keyword(keyword)
            print(f"Successfully inserted {inserted} new articles.")
            break
        else:
            print("Please enter keyword")