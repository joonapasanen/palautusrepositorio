from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

from player_reader import PlayerReader
from player_stats import PlayerStats

seasons = [
    "2018-19",
    "2019-20",
    "2020-21",
    "2021-22",
    "2022-23",
    "2023-24",
    "2024-25",
    "2025-26",
]
nations = [
    "USA",
    "FIN",
    "CAN",
    "SWE",
    "CZE",
    "RUS",
    "SLO",
    "FRA",
    "GBR",
    "SVK",
    "DEN",
    "NED",
    "AUT",
    "BLR",
    "GER",
    "SUI",
    "NOR",
    "UZB",
    "LAT",
    "AUS",
]


def build_table(season, filter_name, players):
    table = Table(title=f"Season {season} players from {filter_name}")
    table.add_column("Player", style="blue")
    table.add_column("Teams", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="green")
    for p in players:
        table.add_row(p.name, p.team, str(p.goals), str(p.assists), str(p.points))
    return table

def select_by_nationality(stats):
    nationality = Prompt.ask("Nationality", choices=nations, default="")
    return nationality, stats.top_scorers_by_nationality(nationality)


def select_by_team(stats):
    teams = sorted({player.team for player in stats.players})
    team = Prompt.ask("Team", choices=teams)
    return team, stats.top_scorers_by_team(team)


def select_players(stats):
    search_by = Prompt.ask(
        "Search players by", choices=["nationality", "team"], default="nationality"
    )
    if search_by == "nationality":
        return select_by_nationality(stats)
    return select_by_team(stats)

# muutos kopiossa
def main():
    console = Console()
    season = Prompt.ask("Season", choices=seasons, default="2024-25")
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))
    filter_name, players = select_players(stats)

    table = build_table(season, filter_name, players)

    console.print(table)


if __name__ == "__main__":
    main()
