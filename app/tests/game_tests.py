import unittest
from app.models.game import Game
from app.models.player import Player


class TestGame(unittest.TestCase):

    def test_fight__P1_win(self):
        self.P1 = Player("Maeve", "Rock")
        self.P2 = Player("Dolores", "Paper")
        self.game_1 = Game(self.P2, self.P1)
        self.assertEqual("Dolores Wins!", self.game_1.fight(self.P1, self.P2))
    
    def test_fight__P1_lose(self):
        self.P1 = Player("Maeve", "Rock")
        self.P3 = Player("Bernard", "Scissors")
        self.game_2 = Game(self.P1, self.P3)
        self.assertEqual("Maeve Wins!", self.game_2.fight(self.P1, self.P3))
    
    def test_fight__draw(self):
        self.P3 = Player("Bernard", "Scissors")
        self.P4 = Player("William", "Scissors")
        self.game_3 = Game(self.P3, self.P4) 
        self.assertEqual("DRAW!", self.game_3.fight(self.P3, self.P4))

    def test_fight__invalid_response(self):
        self.P5 = Player("Man In Black", "Dammit I'm Mad")
        self.P4 = Player("William", "Scissors")
        self.game_4 = Game(self.P5, self.P4) 
        self.assertEqual("DOES NOT COMPUTE!!!!", self.game_4.fight(self.P5, self.P4))