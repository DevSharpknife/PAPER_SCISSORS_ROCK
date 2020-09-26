import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
            self.player_1 = Player("Dave", "Rock")
            self.player_2 = Player("Other Dave", "Paper")
            self.game = Game(self.player_1, self.player_2)

    def test_battle(self):
        self.assertEqual("Other Dave Wins!", self.game.battle(self.player_1.choice, self.player_2.choice))
