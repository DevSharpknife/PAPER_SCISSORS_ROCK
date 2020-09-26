class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def battle(self, choice_1, choice_2):
        if player_1.choice == player_2.choice:
            return "DRAW!"
        elif player_1.choice == "Paper" and player_2.choice == "Scissors":
            return f"{player_2.name} wins!"
        elif player_1.choice == "Paper" and player_2.choice == "Rock":
            return f"{player_1.name} wins!"
        elif player_1.choice == "Scissors" and player_2.choice == "Paper":
            return f"{player_1.name} wins!"
        elif player_1.choice == "Scissors" and player_2.choice == "Rock":
            return f"{player_2.name} wins!"
        elif player_1.choice == "Rock" and player_2.choice == "Rock":
            return f"{player_1.name} wins!"
        elif player_1.choice == "Rock" and player_2.choice == "Rock":
            return f"{player_1.name} wins!"
        else:
            return "DOES NOT COMPUTE!!!!""
