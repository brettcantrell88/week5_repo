import random

class Player:
    def __init__(self, name):
        self.name = name
        self.gestures = ["Rock, Paper, Scissors, Lizard, Spock"]
        self.chosen_gesture = ""
        self.score = 0


    def choose_gesture(self):
        self.choose_gesture = random.choice(self.gestures)
        print(f"{self.name} has chosen {self.chosen_gesture} as their choice.")
        