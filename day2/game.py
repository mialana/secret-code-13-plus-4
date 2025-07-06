import questionary
import random

# STEP 1: Ask player if they want to start the game
response1 = questionary.confirm("Do you want to roll the dice?").ask()

if response1:
    print("Cool! Let's get started...")

    # STEP 2: Create a random number from 1 to 9, store it, and show to player
    MIN = 1
    MAX = 9

    jk = 0
    while jk < 6:
        print(jk) # indent
        jk = jk+1

        # Generate a random number for our dice result
        dice_result = random.randint(MIN, MAX)
        print(f"You got {dice_result}")
    
# STEP 2: Generate path of numbers, last one is always 20
response2 = questionary.confirm("Do you want to print the path of numbers?").ask()

# RULES FOR VARIABLES:
# 1. Can't be only numbers
# 2. No spaces
# 3. No symbols: @ ! ? , .
# 4. BUT it can contain an underscore: _

if response2:
    MIN_NUM = 1
    MAX_NUM = 19
    for abcdefghijklmnopqrstuvwxyz in range(0, 15):
        print(abcdefghijklmnopqrstuvwxyz)
        path = random.randint(MIN_NUM, MAX_NUM)

        print(f"A number on your path is {path}")
    
