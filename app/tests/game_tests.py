import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
            self.player_1 = Player("Maeve", "Rock")
            self.player_2 = Player("Dolores", "Paper")
            self.player_3 = Player("Bernard", "Scissors")
            self.player_4 = Player("William", "Scissors")
            self.game = Game(self.player_1, self.player_2)
            self.game_2 = Game(self.player_1, self.player_3)
            self.game_3 = Game(self.player_3, self.player_4)

    def test_battle__P1_win(self):
        self.assertEqual("Dolores Wins!", self.game.battle(self.player_1, self.player_2))
    
    def test_battle__P1_lose(self):
        self.assertEqual("Maeve Wins!", self.game_2.battle(self.player_1, self.player_3))
    
    def test_battle__draw(self):
        self.assertEqual("DRAW!", self.game_3.battle(self.player_3, self.player_4))

    
