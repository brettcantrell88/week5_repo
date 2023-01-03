from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        user_input = int(input("Press 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, 4 for Spock. "))
        self.chosen_gesture = self.gestures[user_input]
        print(f"{self.name} has chosen {self.chosen_gesture} as their choice. ")
    
