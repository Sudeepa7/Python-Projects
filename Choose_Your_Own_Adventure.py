name = input("Type your name : ")
print("Welcome", name , "to this adventure!")

answer = input ("You are on a dirt road, it has come to an end and end you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around  and type swim to swim across : ")
    if answer == "swim":
        print("You swim across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for may miles, ran out of water and you lost the game.")
    else : 
        print("Not a valid input. You lose.")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to across it or head back (cross/back)? ")
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        if answer == "yes":
            print("You talk to the stratger. And he give you gold and you win! :)")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else : 
            print("Not a valid input. You lose.")
    else : 
        print("Not a valid input. You lose.")
else :
    print("Not a valid input. You lose.")

print("thank you for trying", name)
