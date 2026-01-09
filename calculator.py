import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def calculator():
    add = lambda a , b: a+b
    sub = lambda a , b: a-b
    mul = lambda a , b: a*b
    div = lambda a , b: a/b

    speak("Select Options:")
    speak("1. Add")
    speak("2. Subtract")
    speak("3. Multiplication")
    speak("4. Division")

    try:
        choice = input("Enter Your choice(1/2/3/4): ")
        x = float(input("Enter your first number: "))
        y = float(input("Enter your second number: "))

        if choice=="1":
            print("Result:" , add(x,y))
        elif choice=="2":
            print("Reslult:", sub(x,y))
        elif choice=="3":
            print("Reslult:", mul(x,y))
        elif choice=="4":
            try:
                print("Reslult:", div(x,y))
            except ZeroDivisionError:
                print("Errpr: Cannot Divide by Zero")
            else:
                print("Invalid Center")

    except ValueError:
        print("Error Please enter numbers only!")

calculator()






