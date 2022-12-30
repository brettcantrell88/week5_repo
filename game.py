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
        

    def run_game(self):
        self.game_instructions()
        self.choose_players()
        self.play_hands()
        self.play_hands()

    def game_instructions(self):
        print("Here are the instructions for the game!")
        print()
        print("rock crushes lizard")
        print("rock crushes scissors")
        print("paper covers rock")
        print("paper disproves spock")
        print("scissor cuts paper")
        print("scissors decaptitates lizard")
        print("lizard poisons spock")
        print("lizard eats paper")
        print("spock smashes scissors")
        print("spock vaporizes rock")

    def choose_players(self):
        user_choice = input("Enter 1 for single player and 2 for multiplayer. ")
        if user_choice == "1":
            self.player_two = AI("T1000")
        elif user_choice == "2":
            user_name = input("Enter Player Two's name. ")
            self.player_two = Human(user_name)

    def play_hands(self):
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("It is a tie, keep playing.")
        elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Scissors":
            print("Player One wins")
            self.player_one.score += 1
        elif self.player_one.chosen_gesture == "Rock" and self.player_two.chosen_gesture == "Lizard":
            print("Player One wins")
            self.player_one.score += 1
        elif self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Rock":
            print("Player One wins")
            self.player_one.score += 1
        elif self.player_one.chosen_gesture == "Paper" and self.player_two.chosen_gesture == "Spock":
            print("Player One wins")
            self.player_one.score += 1
        elif self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Paper":
            print("Player One wins")
            self.player_one.score += 1
        elif self.player_one.chosen_gesture == "Scissors" and self.player_two.chosen_gesture == "Lizard":
            print("Player One wins")
            self.player_one.score += 1
        elif self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Spock":
            print("Player One wins")
            self.player_one.score += 1
        elif self.player_one.chosen_gesture == "Lizard" and self.player_two.chosen_gesture == "Paper":
            print("Player One wins")
            self.player_one.score += 1
        elif self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Scissors":
            print("Player One wins")
            self.player_one.score += 1
        elif self.player_one.chosen_gesture == "Spock" and self.player_two.chosen_gesture == "Rock":
            print("Player One wins")
            self.player_one.score += 1
      