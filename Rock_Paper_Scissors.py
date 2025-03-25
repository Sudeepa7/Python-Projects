import random

user_win = 0
computer_win = 0

options = ["rock","paper","scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit : ".lower())
    if user_input == "q":
        break

    if user_input not in options :
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You win!")
        user_win += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_win += 1
        continue
    
    elif user_input == "scissor" and computer_pick == "paper":
        print("You win!")
        user_win += 1
        continue

    else : 
        print("You lost!")
        computer_win += 1
        continue

print("You won" , user_win , "times.")
print("Computer won" , computer_win , "times.")
print("Good bye!")