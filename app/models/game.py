class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def fight(self):
        if self.player_1.choice == self.player_2.choice:
            return "DRAW!"
        elif self.player_1.choice == "Rock" and self.player_2.choice == "Paper" or self.player_1.choice == "Scissors" and self.player_2.choice == "Rock" or self.player_1.choice == "Paper" and self.player_2.choice == "Scissors":
            return f"{self.player_2.handle} Wins!"
        elif self.player_1.choice == "Rock" and self.player_2.choice == "Scissors" or self.player_1.choice == "Scissors" and self.player_2.choice == "Paper" or self.player_1.choice == "Paper" and self.player_2.choice == "Rock":
            return f"{self.player_1.handle} Wins!"
        else:
            return "DOES NOT COMPUTE!!!!"