# Rock, Paper, Scissors game

import random

options = ("rock", "paper", "scissors")
player = None
coumputer = random.choice(options)
running = True

while running:
    player = None
    coumputer = random.choice(options)

    while player not in options:
        player = input(f"Pick a choice (rock, paper or scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {coumputer}")

    if player == coumputer:
        print("It's a Tie!")
    elif player == "scissors" and coumputer == "paper":
        print("You Win!")
    elif player == "rock" and coumputer == "paper":
        print("You Win!")
    elif player == "paper" and coumputer == "rock":
        print("You Win!")
    else:
        print("You Lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print ("Thanks for playing!")
