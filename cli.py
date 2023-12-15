import argparse

from constants import LEAGUES


class CLI:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(prog="Football Standings CLI")
        self.parser.add_argument(
            "league",
            help=self._league_help_text(),
        )

    def _league_help_text(self):
        txt = "Type: "
        for k, v in LEAGUES.items():
            txt += f"'{k}' for {v}, "
        return txt[0:-2]

    def get_parse_args(self):
        return self.parser.parse_args()
