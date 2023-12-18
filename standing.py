from rich.table import Table
from pyboxen import boxen


class Standing:
    def __init__(self, data) -> None:
        self.table = Table(show_header=True, header_style="bold magenta")
        self._add_columns(data)
        self._add_rows(data)

    def _add_columns(self, data) -> None:
        for header in data["column"]:
            self.table.add_column(header)

    def _add_rows(self, data) -> None:
        for row in data["rows"]:
            self.table.add_row(
                f"{row['rank']} {row['club']}",
                row["played"],
                row["won"],
                row["draw"],
                row["loss"],
                row["goals_scored"],
                row["goals_conceded"],
                row["points"],
            )

    def show_standing(self) -> None:
        print(boxen(self.table))
