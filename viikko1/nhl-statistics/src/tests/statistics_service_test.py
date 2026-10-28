import unittest

from player import Player
from statistics_service import SortBy, StatisticsService


class StubReader:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.test_player1 = Player(
            name="Rantanen", team="Dallas Stars", goals=32, assists=55
        )
        self.test_player2 = Player(
            name="Gudas", team="Anaheim Ducks", goals=3, assists=7
        )
        self.test_player3 = Player(
            name="Suzuki", team="Montreal Canadiens", goals=20, assists=35
        )
        player_reader = StubReader(
            [self.test_player1, self.test_player2, self.test_player3]
        )
        self.statistics_service = StatisticsService(player_reader)

    def test_etsi_pelaaja(self):
        player = self.statistics_service.search("Rantanen")
        self.assertEqual(self.test_player1, player)

    def test_etsi_olematon_pelaaja(self):
        player = self.statistics_service.search("Meikalainen")
        self.assertEqual(player, None)

    def test_etsi_joukkue(self):
        team = self.statistics_service.team("Dallas Stars")
        self.assertEqual(team, [self.test_player1])

    def test_parhaat_pistemiehet_jarjestyksessa(self):
        ranked_on_points = self.statistics_service.top(2, SortBy.POINTS)
        self.assertEqual(
            ranked_on_points, [self.test_player1, self.test_player3, self.test_player2]
        )

    def test_parhaat_maalintekijat_jarjestyksessa(self):
        ranked_on_goals = self.statistics_service.top(2, SortBy.GOALS)
        self.assertEqual(
            ranked_on_goals, [self.test_player1, self.test_player3, self.test_player2]
        )

    def test_parhaat_syottajat_jarjestyksessa(self):
        ranked_on_goals = self.statistics_service.top(2, SortBy.ASSISTS)
        self.assertEqual(
            ranked_on_goals, [self.test_player1, self.test_player3, self.test_player2]
        )
