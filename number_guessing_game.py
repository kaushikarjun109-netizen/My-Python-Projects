import random
def number_guessing_name():
    secret_number = random.randint(1,100)
    print("Welcome to numbering guessing name")
    print("Choose the number between 1 to 100")


    attempts = 0
    guess = None

    while guess != secret_number:
        guess = int(input("Enter uour number: "))
        attempts = attempts+1

        if guess < secret_number :
            print("Too Low")
        elif guess > secret_number:
            print("Too high")
        else:
            print(f"Congrats you guess the right number {secret_number}")


        print(f"The number of attempts you take is {attempts}")    

number_guessing_name()


