from cli import CLI
from fetcher import fetch_standing_data
from standing import Standing

from constants import LEAGUES


def main():
    parser = CLI()
    args = parser.get_parse_args()

    data = fetch_standing_data(LEAGUES[args.league])

    standing = Standing(data)
    standing.show_standing()


if __name__ == "__main__":
    main()
