import questionary
import random

# STEP 1: Ask player if they want to start the game
response1 = questionary.confirm("Do you want to roll the dice?").ask()

if response1:
    print("Cool! Let's get started...")

    # STEP 2: Create a random number from 1 to 9, store it, and show to player
    MIN = 1
    MAX = 9

    dice = [1,2,3,4,5,6]

    jk = 0
    while jk < 6:
        # Generate a random number for our dice result
        dice_result = random.randint(MIN, MAX)
        print(f"You got {dice_result}")

        dice[jk] = dice_result

        jk = jk+1

    print(f"Your dice numbers are {dice}")


#####

    
# STEP 2: Generate path of numbers, last one is always 20
response2 = questionary.confirm("Do you want to print the path of numbers?").ask()


if response2:
    MIN_NUM = 1
    MAX_NUM = 19

    LASER_PATH = [-1] * 6
    LASER_PATH[5] = 20

    for abcdefghijklmnopqrstuvwxyz in range(0, 5):
        path = random.randint(MIN_NUM, MAX_NUM)

        LASER_PATH[abcdefghijklmnopqrstuvwxyz] = path

    print(f"Your entire path is {LASER_PATH}")

answer = questionary.text("What do you want to do with the numbers?").ask()

print(answer)