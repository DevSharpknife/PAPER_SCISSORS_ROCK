import unittest
from app.models.game import Game
from app.models.player import Player


class TestGame(unittest.TestCase):

    def test_battle__P1_win(self):
        self.P1 = Player("Maeve", "Rock")
        self.P2 = Player("Dolores", "Paper")
        self.game_1 = Game(self.P2, self.P1)
        self.assertEqual("Dolores Wins!", self.game_1.battle(self.P1, self.P2))
    
    def test_battle__P1_lose(self):
        self.P1 = Player("Maeve", "Rock")
        self.P3 = Player("Bernard", "Scissors")
        self.game_2 = Game(self.P1, self.P3)
        self.assertEqual("Maeve Wins!", self.game_2.battle(self.P1, self.P3))
    
    def test_battle__draw(self):
        self.P3 = Player("Bernard", "Scissors")
        self.P4 = Player("William", "Scissors")
        self.game_3 = Game(self.P3, self.P4) 
        self.assertEqual("DRAW!", self.game_3.battle(self.P3, self.P4))