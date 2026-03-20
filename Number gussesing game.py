# Number gussesing game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("WELCOME TO THE NUMBER GAME!")
print(f"Enter a number btween {lowest_num} and {highest_num}: ")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("THAT NUMBER IS OUT OF RANGE")
            print(f"Please Enter a number btween {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print(f"CORRECT! The answer was: {answer}")
            print(f"Your number of guesses were: {guesses}")
            is_running = False

    else:
        print("INVALID GUESS!")
        print(f"Please Enter a number btween {lowest_num} and {highest_num}")

if guesses >= 10:
    print("Sounds like a skill issue! 🤡")
elif guesses >= 5:
    print("Good! But you can do better 🗿")
else:
    print("Ayoo are u even a human? 💀")