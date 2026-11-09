import textwrap

import questionary

from src.collector.source import find_from_keyword
from rich import print
from rich.console import Console
from rich.panel import Panel


def collect():

    console = Console()

    while True:
        # Ask for user keyword, then search it up
        keyword = questionary.text("What would you like to search?").ask()

        if keyword is None:
            break

        if keyword:
            # This function returns number of news that was inserted into the db

            print("\nPlease wait...\n")

            result = find_from_keyword(keyword)

            found = result[0]
            parsed = result[1]
            inserted = result[2]
            skipped = parsed - inserted

            parsed_summary = f"""
                Found:                {found}
                Parsed:               {parsed}
                Inserted:             {inserted}
                Skipped / Stored:     {skipped}
            """

            console.print(
                Panel(
                    textwrap.dedent(parsed_summary).strip(),
                    expand=False
                ),
                '\n'
            )

            break
        else:
            print("Please enter keyword")