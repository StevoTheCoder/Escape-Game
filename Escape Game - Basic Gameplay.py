import random


def playGame():
    randomNum = random.randint(1,100)

    while True:
        PIN = int(input("Enter your guess (1-100): "))
        if PIN == randomNum:
            print("Conrgatulations! You've escaped! ")
            break
        elif PIN > randomNum:
            print("Too high, Try again. ")

        else:
                print("Too low, Try again. ")

playGame()
    
playAgain = str(input("Do you want to play again? (Yes/No): "))

if playAgain == "Yes":
    playGame()

else:
    print("Thanks for playing!")







