from mode.analyze import analyze
from mode.collect import collect
from typer import Typer
from rich.console import Console

logo = """
        [bold red]
        88""Yb .dP"Y8 .dP"Y8     88b 88 888888 Yb        dP .dP"Y8     .dP"Y8  dP""b8 88""Yb    db    88""Yb 888888 88""Yb 
        88__dP `Ybo." `Ybo."     88Yb88 88__    Yb  db  dP  `Ybo."     `Ybo." dP   `" 88__dP   dPYb   88__dP 88__   88__dP 
        88"Yb  o.`Y8b o.`Y8b     88 Y88 88""     YbdPYbdP   o.`Y8b     o.`Y8b Yb      88"Yb   dP__Yb  88\"""  88""   88"Yb  
        88  Yb 8bodP' 8bodP'     88  Y8 888888    YP  YP    8bodP'     8bodP'  YboodP 88  Yb dP\"""\"Yb 88     888888 88  Yb
        [/bold red]
        """

app = Typer(rich_markup_mode="rich")
console = Console()

@app.command()
def main():
    console.print(logo)

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


if __name__ == "__main__":
    main()