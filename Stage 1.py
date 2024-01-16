import random

def Stage1():
    randomNum = random.randint(1, 100)
    playersLives = 6
    playersGuess = None

    while True:
        PIN = int(input("Enter your guess (1-100): "))
        playersGuess = PIN  # Assign the guessed PIN to playersGuess
        
        if PIN == randomNum:
            print("Congratulations! You've escaped!")
            break
        elif PIN > randomNum:
            print("Too high, Try again.")
        else:
            print("Too low, Try again.")
        
        playersLives -= 1  # Decrement player's lives after each guess

        if playersLives == 0:
            print(f"Game over! Your closest guess was {playersGuess}. The correct PIN was {randomNum}.")
            break

Stage1()
    
playAgain = str(input("Do you want to play again? (Yes/No): "))

if playAgain == "Yes":
    Stage1()

else:
    print("Thanks for playing!")
