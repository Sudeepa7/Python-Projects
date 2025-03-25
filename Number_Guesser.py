import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0 : 
        print("Please type a number larger than 0 next time.")
        quit()

else : 
    print("Please type a number next time.")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

while True : 
    guesses += 1
    guessed_number = input("Guess the number : ")

    if guessed_number.isdigit() :
        guessed_number = int(guessed_number)
    
    else : 
        print("Please type a number next time.")
        continue

    if guessed_number == random_number :
        print("Your guess is correct!")
        break

    elif guessed_number < random_number :
        print("Your guess is less than the number!")
        
    else :
        print("Your guess is higher than the number!")
        continue

print("You got it in" ,guesses, "guess.")



