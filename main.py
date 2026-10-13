from mode.analyze import analyze
from mode.collect import collect

print("RSS News Scraper\n")

while True:
    print("=" * 40)
    print("Mode Selection")
    print("[1]: Collect news from RSS")
    print("[2]: Analyze existing news")
    print("[0]: Exit")
    print("=" * 40)

    while True:
        mode = int(input("Enter your mode: "))

        match mode:
            case 1:
                collect()
                break
            case 2:
                analyze()
                break
            case 0:
                exit()
            case _:
                print("Invalid command. Try again.")
