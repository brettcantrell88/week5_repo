# scissor cuts paper
# paper cover rock
# rock crushes lizard
# lizard poisons spock
# spock smashes scissors
# scissors decapitates lizard
# lizard eats paper
# paper disproves spock
# spock vaporizes rock
# rock crushes scissors
from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.player_one = Human("Player One")
        self.player_two = None
        pass


    def start_game(self):
        self.game_instructions()
        self.choose_players()

    def game_instructions(self):
        print("Here are the instructions for the game!")
        print()
        print("scissor cuts paper")
        print("paper covers rock")
        print("rock crushes lizard")
        print("lizard poisons spock")
        print("spock smashes scissors")
        print("scissors decaptitates lizard")
        print("lizard eats paper")
        print("paper disproves spock")
        print("spock vaporizes rock")
        print("rock crushes scissors")

    def choose_players(self):
        user_choice = input("Enter 1 for single player and 2 for multiplayer. ")
        if user_choice == 1:
            self.player_two = AI("T1000")
        elif user_choice == 2:
            user_name = input("Enter Player Two's name. ")
        
