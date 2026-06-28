import random


def save_score(username, score):
    
    with open("highscores.txt", "a") as file:
        
        file.write(f"{username}: {score}\n")


def show_leaderboard():
    print("\n====== LEADERBOARD ======")

    #  opening the score file
    try:
        with open("highscores.txt", "r") as file:

            # Create an empty list to store the scores
            scores = []

            #looping through the file
            for line in file:

                
                name, score = line.strip().split(": ")
                scores.append((name, int(score)))

            # Sort the scores from highest to lowest
            scores.sort(key=lambda x: x[1], reverse=True)

           
            if len(scores) == 0:
                print("No scores yet.")

            else:
                # Display only the top 10 scores
                for i, (name, score) in enumerate(scores[:10], start=1):
                    print(f"{i}. {name} - {score} points")

    # If the file does not exist, display a message
    except FileNotFoundError:
        print("No leaderboard available yet.")



print("===== GUESS THE NUMBER GAME =====")

# Ask the player for their name
username = input("Enter your name: ")

# Display the difficulty levels
print("\nChoose Difficulty")
print("1. Easy (10 tries)")
print("2. Medium (7 tries)")
print("3. Hard (5 tries)")

# Ask the player to choose a difficulty
choice = input("Enter choice (1-3): ")

# Set the number of attempts depending on the difficulty
if choice == "1":
    attempts = 10

elif choice == "2":
    attempts = 7

elif choice == "3":
    attempts = 5

# If the user enters an invalid option, use Easy mode
else:
    print("Invalid choice. Defaulting to Easy.")
    attempts = 10


# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Count how many incorrect guesses the player has made
wrong_guesses = 0

print("\nI have chosen a number between 1 and 100.")
print(f"You have {attempts} attempts.\n")


# Main game loop

while attempts > 0:

   
    try:
        guess = int(input("Enter your guess: "))

    except ValueError:
        print("Please enter a valid number.")
        continue

    # Check whether the guess is correct
    if guess == secret_number:

        print("\n Congratulations!")
        print("You guessed the correct number!")

        # Calculate the player's score
      
        score = attempts * 10

        print("Your score:", score)

        # Save the player's score
        save_score(username, score)

        # Exit the game loop
        break

    
    elif guess < secret_number:
        print("Too Low!")

    
    else:
        print("Too High!")

    attempts -= 1

    # Increase the number of wrong guesses
    wrong_guesses += 1

    # Display the remaining attempts if the game is not over
    if attempts > 0:
        print("Remaining attempts:", attempts)

    
    if wrong_guesses == 3:

        print("\n------ HINT ------")

        # Check whether the secret number is even or odd
        if secret_number % 2 == 0:
            print("The number is EVEN.")
        else:
            print("The number is ODD.")

        # Check whether the number is divisible by 5
        if secret_number % 5 == 0:
            print("The number is divisible by 5.")
        else:
            print("The number is NOT divisible by 5.")

        print("------------------")

else:
    print("\n Game Over!")
    print("The correct number was:", secret_number)


# Display the leaderboard at the end of the game
print()
show_leaderboard()