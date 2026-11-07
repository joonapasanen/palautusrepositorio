import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def get_players(self):
        return [
            Player(
                {
                    "name": "Mikko",
                    "nationality": "FIN",
                    "team": "CAR",
                    "goals": 10,
                    "assists": 20,
                }
            ),
            Player(
                {
                    "name": "Alex",
                    "nationality": "CAN",
                    "team": "CAR",
                    "goals": 30,
                    "assists": 10,
                }
            ),
            Player(
                {
                    "name": "Pekka",
                    "nationality": "FIN",
                    "team": "DAL",
                    "goals": 20,
                    "assists": 5,
                }
            ),
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def test_top_scorers_by_nationality(self):
        players = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual([player.name for player in players], ["Mikko", "Pekka"])

    def test_top_scorers_by_team(self):
        players = self.stats.top_scorers_by_team("CAR")

        self.assertEqual([player.name for player in players], ["Alex", "Mikko"])

    def test_top_goal_scorers(self):
        players = self.stats.top_goal_scorers(2)

        self.assertEqual([player.name for player in players], ["Alex", "Pekka"])
