# Ask the user?
# if it tells y than generate the random number
#if it says n than terminate the loop and exit it 
# if user ask anything different print invalid term 
import random

while True:
    choice = input("Enter your choice(y/n): ").lower()
    #For entering in loop and generating random numbers if user wants to
    if choice == "y":
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"number 1: {die1} , number 2: {die2}")
        #If user don't want fo generate number it can deny
    elif choice == "n":
        print("Thankyou")
        #Terminate the code 
        break
    #for ohter than y and n any other input the code will not accept it 
    else:
        print("Invalid Term!!")

