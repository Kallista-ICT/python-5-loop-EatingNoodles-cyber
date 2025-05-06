import random
from unittest import result 

#comment
score = 0
rolls = []

#make message
print("Hello player!")
print("Enter how many time does the dice needs to be rolled.")

#comment
while score < 50:
    input("press to roll")
    die = random.randint(1, 6)
    score += die
    rolls.append(die)

    print(f"show the result of the die: {die}")
    print(f"show the score: {score}")

print("Congratulations! You have reached 50 points!")

#Ask if the user wants to see the history of the rolls
show_history = input("Do you want to see the history of the rolls? (yes/no): ").strip().lower()
if show_history == 'yes':
    print("History of rolls:")
    roll_number = 1
    for roll in rolls:
        print(f"Roll {roll_number}: {roll}")
        roll_number += 1