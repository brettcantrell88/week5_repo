from player import Player
import random


class AI(Player):
    def __init__(self, name):
        super().__init__(name)
    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures)
        print(f"{self.name} has chosen {self.chosen_gesture} as their choice. ")
            
