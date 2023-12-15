from rich.table import Table
from pyboxen import boxen

from cli import CLI
from fetcher import fetch_standing_data

from constants import LEAGUES


parser = CLI()
args = parser.get_parse_args()

data = fetch_standing_data(LEAGUES[args.league])

table = Table(show_header=True, header_style="bold magenta")

for header in data["column"]:
    table.add_column(header)

for row in data["rows"]:
    table.add_row(
        f"{row['rank']} {row['club']}",
        row["played"],
        row["won"],
        row["draw"],
        row["loss"],
        row["goals_scored"],
        row["goals_conceded"],
        row["points"],
    )

print(boxen(table))
