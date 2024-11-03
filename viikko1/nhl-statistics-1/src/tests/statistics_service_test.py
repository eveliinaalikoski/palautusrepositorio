import unittest
from statistics_service import StatisticsService
from player import Player

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
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_search_correct_name(self):
        player = self.stats.search("Semenko")

        self.assertAlmostEqual(player.name, "Semenko")

    def test_search_incorrect_name(self):
        name = self.stats.search("Incorrect")

        self.assertAlmostEqual(name, None)

    def test_players_by_team(self):
        players = self.stats.team("PIT")
        correct = [Player("Lemieux", "PIT", "45", "54")]
        
        self.assertAlmostEqual(players[0].name, correct[0].name)

    def test_players_top(self):
        players = self.stats.top(2)

        correct = [Player("Gretzky", "EDM", 35, 89),
                   Player("Lemieux", "PIT", 45, 54)]
        
        self.assertAlmostEqual(players[0].name, correct[0].name)
