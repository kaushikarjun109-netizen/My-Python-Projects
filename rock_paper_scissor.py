import random
import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait

computer = random.choice([-1,0,1])
youstr = input("Enter your Option: ")
youDict= {"r":-1 , "p":0 , "s" : 1}
revrseDict = {-1:"rock" , 0: "paper", 1:"scissor"}
you = youDict[youstr]

print(f"You choose {revrseDict[you]}\n Computer choose {revrseDict[computer]}")

if computer == you:
    print("It's Draw")
else:
    if(you == 1 and computer == 0):
        print("You win")
    elif(you == 1 and computer == -1 ):
        print("You loose")
    elif(you == 0 and computer == -1 ):
        print("You Win")
    elif(you == 0 and computer == 1 ):
        print("You loose")
    elif(you == -1 and computer == 1 ):
        print("You Win")
    elif(you == -1 and computer == 0 ):
        print("You loose")









