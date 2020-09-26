import unittest
from app.models.player import Player
# from app.models.game import Game

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Dave", "Rock")

    def test_player_handle(self):
        self.assertEqual("Dave", self.player.handle)

    def test_player_choice(self):
        self.assertEqual("Rock", self.player.choice)