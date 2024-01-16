import random  # Import for generating random numbers

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


def Stage2():
    # Generate random numbers for each player
    randomNum1 = random.randint(1, 100)
    randomNum2 = random.randint(1, 100)

    # Player 1 and Player 2 lives and guess variables
    player1Lives = 6
    player1Guesses = None
    
    player2Lives = 6
    player2Guesses = None

    # Loop while both players have lives left - alternate between Player 1 and Player 2
    while player1Lives > 0 and player2Lives > 0:
        # Player 1's turn
        PIN = int(input("Player 1, enter your guess (1-100): "))  # Input Player 1's guess
        player1Guesses = PIN  # Store player 1's guess

        # Check if player 1 guessed correctly
        if PIN == randomNum1:
            print("Player 1 has escaped!")
            break  # End game if Player 1 guessed correctly
        elif PIN > randomNum1:
            print("Player 1: Too high, Try again.")  # Gives hint if guess is too high
        else:
            print("Player 1: Too low, Try again.")  # Gives hint if guess is too low

        player1Lives -= 1  # Decreases player 1's lives by 1 each incorrect guess

        if player1Lives == 0:
            print("Player 1 has lost all lives!")  # Player 1 lost all lives
            break  # End game if player 1 lost all lives

        # Player 2's turn - same loop as the above
        PIN = int(input("Player 2, enter your guess (1-100): "))
        player2Guesses = PIN

        if PIN == randomNum2:
            print("Player 2 has escaped!")
            break
        elif PIN > randomNum2:
            print("Player 2: Too high, Try again.")
        else:
            print("Player 2: Too low, Try again.")

        player2Lives -= 1

        if player2Lives == 0:
            print("Player 2 has lost all lives!")
            break

    # Will announce the winner if they guess the correct PIN
    if player2Guesses == randomNum2:
        print("Player 2 wins!")
    if player1Guesses == randomNum1:
        print("Player 1 wins!")
    if player1Lives == 0 and player2Lives == 0:
        print("Game over!")  # Game ends if both players lost all lives

Stage2()  # Run the Stage2 of the game
