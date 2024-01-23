import random

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number(1-100): ")

    if player_input.isdigit():
        print("Invalid input. Try again...")
        continue

    player_number = int(input())

    if player_number == computer_number:
        print("You guess it!")
        break