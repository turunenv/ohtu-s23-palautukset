from player import Player
from statistics_service import StatisticsService, SortBy
import unittest



class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
    
class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search_with_correct_name_returns_the_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")

    def test_search_with_nonexistent_name_returns_none(self):
        player = self.stats.search("Krri")

        self.assertEqual(player, None)

    def test_team_method_returns_correct_players(self):
        players = self.stats.team("EDM")
        edm_players = list(filter(
            lambda player: player.team == "EDM",
            players
        ))
        print(edm_players)

        self.assertEqual(len(players), len(edm_players))

    def test_top_returns_correct_players(self):
        players = self.stats.top(2)

        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")

    def test_top_with_points_returns_correct_players(self):
        players = self.stats.top(2, SortBy.POINTS)

        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")

    def test_top_with_goals_returns_correct_players(self):
        players = self.stats.top(2, SortBy.GOALS)

        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")
    
    def test_top_with_assists_returns_correct_players(self):
        players = self.stats.top(2, SortBy.ASSISTS)

        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Yzerman")


        