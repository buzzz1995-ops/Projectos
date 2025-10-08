import tkinter as tk
from enum import Enum
import random


# Choices
class Choice(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"

    @staticmethod
    def beats(choice1, choice2):
        rules = {
            Choice.ROCK: Choice.SCISSORS,
            Choice.PAPER: Choice.ROCK,
            Choice.SCISSORS: Choice.PAPER
        }
        return rules[choice1] == choice2


# Player
class Player:
    def __init__(self, name, is_computer=False):
        self.name = name
        self.is_computer = is_computer
        self.choice = None

    def make_choice(self, choice=None):
        if self.is_computer:
            self.choice = random.choice(list(Choice))
        else:
            self.choice = choice


# Game
class Game:
    def __init__(self, player1, player2, label_result):
        self.player1 = player1
        self.player2 = player2
        self.label_result = label_result

    def play_round(self, choice):
        self.player1.make_choice(choice)
        self.player2.make_choice()

        result = f"{self.player1.name} chose {self.player1.choice.value}\n"
        result += f"{self.player2.name} chose {self.player2.choice.value}\n"

        if self.player1.choice == self.player2.choice:
            result += "It's a tie!"
        elif Choice.beats(self.player1.choice, self.player2.choice):
            result += f"{self.player1.name} wins!"
        else:
            result += f"{self.player2.name} wins!"

        self.label_result.config(text=result)


# Tkinter UI
root = tk.Tk()
root.title("Rock Paper Scissors")

label = tk.Label(root, text="Choose your move:", font=("Arial", 14))
label.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12), justify="left")
label_result.pack(pady=20)

# Players
p1 = Player("You")
p2 = Player("Computer", is_computer=True)
game = Game(p1, p2, label_result)


def make_choice(choice):
    game.play_round(choice)


# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

for choice in Choice:
    btn = tk.Button(btn_frame, text=choice.value.capitalize(),
                    width=10, height=2,
                    command=lambda c=choice: make_choice(c))
    btn.pack(side="left", padx=5)

root.mainloop()
