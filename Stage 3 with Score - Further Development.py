import random

def get_valid_input(player):
    while True:
        PIN = input(f"{player}, enter your guess (1-100): ")
        if PIN.isdigit():
            PIN = int(PIN)
            if 1 <= PIN <= 100:
                return PIN
            else:
                print("Please enter a number between 1 and 100.")
        else:
            print("Please enter a valid number.")

def Stage3():
    randomNum1 = random.randint(1, 100)
    randomNum2 = random.randint(1, 100)

    player1Lives = 6
    player2Lives = 6

    player1Score = 0
    player2Score = 0

    while player1Lives > 0 and player2Lives > 0:
        player1Guess = get_valid_input("Player 1")
        if player1Guess == randomNum1:
            print("Player 1 has escaped!")
            player1Score += 1 #Increases Player 1's score by 1
            break
        elif player1Guess > randomNum1:
            print("Player 1: Too high, Try again.")
        else:
            print("Player 1: Too low, Try again.")
        player1Lives -= 1
        if player1Lives == 0:
            print("Player 1 has lost all lives!")
            break

        player2Guess = get_valid_input("Player 2")
        if player2Guess == randomNum2:
            print("Player 2 has escaped!")
            player2Score += 1 #Increase Player 2's score by 1
            break
        elif player2Guess > randomNum2:
            print("Player 2: Too high, Try again.")
        else:
            print("Player 2: Too low, Try again.")
        player2Lives -= 1
        if player2Lives == 0:
            print("Player 2 has lost all lives!")
            break

    if player1Guess == randomNum1:
        print("Player 1 wins!")
    elif player2Guess == randomNum2:
        print("Player 2 wins!")
    else:
        print("Game over!")

    print(f"Player 1's Score: {player1Score}: ")
    print(f"Player 2's Score: {player2Score}: ")


Stage3()


playAgain = str(input("Do you want to play again? (yes/no): "))

if playAgain == "Yes":
    Stage3()

else:
    print("Thanks for playing!")


