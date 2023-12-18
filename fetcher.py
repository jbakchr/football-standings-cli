import requests
from bs4 import BeautifulSoup

table_data = [
    "played",
    "won",
    "draw",
    "loss",
    "goals_scored",
    "goals_conceded",
    "points",
]


def _get_thead_data(table):
    table_header = table.find("thead")

    thead_headers = table_header.find_all("th")

    head_data = []
    for th in thead_headers:
        span = th.find("span")
        head_data.append(span.text.strip())
    return head_data


def _get_tbody_data(table):
    table_body = table.find("tbody")

    table_rows = table_body.find_all("tr")

    row_data = []
    for tr in table_rows:
        row = {}

        row["rank"] = tr.find("span", {"class": "rank-number"}).text
        row["club"] = tr.a.span.text

        divs = tr.find_all("div", {"class": "data-wrapper"})

        for i, div in enumerate(divs):
            row[table_data[i]] = div.span.text

        row_data.append(row)

    return row_data


def fetch_standing_data(league):
    # Get data
    response = requests.get(f"https://bold.dk/fodbold/stillinger/{league}")
    soup = BeautifulSoup(response.text, "html.parser")

    # data to return
    data = {"column": [], "rows": []}

    table = soup.find("table")

    # Get table headers
    data["column"] = _get_thead_data(table)

    # Get table rows
    data["rows"] = _get_tbody_data(table)

    return data
