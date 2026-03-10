import random

while True:
    print("\nYes = Play")
    print("No = Exit")
            
    roll = input("enter choice: ").capitalize()

    if roll == "Yes":
        num = random.randrange(1,7)
        print("Dice rolled: ",num)
    elif roll == "No":
        print("see you later")
        break
    else:
        print("Invalid choice! Please type Yes or No.")
            