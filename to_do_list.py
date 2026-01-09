#guess the number between 1 to 100
# create a loop until you create an correct guess
# giving an hint for guess an correct one
import random

random_num = random.randint(1,100)
while True:
    try:
        guess = int(input("Enter your number between(1 and 100) : ")) 
        if  random_num > guess:
            print("Too Low")
        elif random_num < guess:
            print("Too High")
        else:
            print(f"Congrats {random_num} is the correct number ")
    except ValueError:
        print("Invalid context")

