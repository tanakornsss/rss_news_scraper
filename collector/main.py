from source import find_from_keyword

# Ask for user keyword, then search it up
keyword = str(input("Enter your search keyword: ")).strip()

if keyword:
    # This function returns number of news that was inserted into the db
    inserted = find_from_keyword(keyword)
    print(f"Successfully inserted {inserted} new articles.")
else:
    print("Please enter keyword")
