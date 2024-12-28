import random

def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 15.")
    
    # Generate a random number between 1 and 15
    number_to_guess = random.randint(1, 15)
    attempts = 0
    
    # Keep asking the player for guesses until they get the correct number
    while True:
        guess = input("Enter your guess: ")
        
        # Check if input is a number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break

# Run the game
guess_number()

