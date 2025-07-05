import questionary
import random

# STEP 1: Ask player if they want to start the game
response = questionary.confirm("Do you want to roll the dice?").ask()

if response:
    print("Cool! Let's get started...")

    # STEP 2: Create a random number from 1 to 9, store it, and show to player
    MIN = 1
    MAX = 9

    # Generate a random number for our dice result
    dice_result = random.randint(MIN, MAX)
    print(f"You got {dice_result}")



