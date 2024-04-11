import random

# Define the possible colors for the code and the game parameters
COLORS = ["R", "G", "Y", "B", "O", "W"]
TRIES = 10  # Maximum number of attempts a player has to guess the code
CODE_LENGTH = 4  # The length of the secret code

def generate_code():
    #Generates a random secret code from the available colors
    code = []
    for _ in range(CODE_LENGTH):  # Repeat for the length of the code
        color = random.choice(COLORS)  # Randomly select a color
        code.append(color)  # Add the selected color to the code
    return code  # Return the generated secret code

def guess_code():
    #Prompts the player for a guess and validates it
    while True:
        guess = input("Guess: ").upper().strip()  # Get guess, remove spaces, and uppercase it

        guess_list = list(guess)  # Convert the guess string into a list of characters

        # Check if the guess is the correct length
        if len(guess_list) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue  # Prompt for another guess if incorrect length

        # Check for invalid colors in the guess
        invalid_color_found = False
        for color in guess_list:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                invalid_color_found = True
                break  # Stop checking further if an invalid color is found
        
        # If all colors in the guess are valid, return the guess
        if not invalid_color_found:
            return guess_list

def check_code(guess, real_code):
    # Compares the guess to the secret code and counts correct positions and colors
    correct_pos = 0  # Count of correct colors in the correct positions
    guess_counts = {}
    real_code_counts = {}
    
    # Populate counts for colors not in the correct position
    for i in range(CODE_LENGTH):
        if guess[i] == real_code[i]:
            correct_pos += 1  # Increment for correct color and position
        else:
            # Count occurrences of each color in guess and real code for later comparison
            guess_counts[guess[i]] = guess_counts.get(guess[i], 0) + 1
            real_code_counts[real_code[i]] = real_code_counts.get(real_code[i], 0) + 1

    incorrect_pos = 0  # Initialize count of correct colors in incorrect positions
    # Calculate incorrect positions based on the minimum occurrences of each color
    for color in guess_counts:
        if color in real_code_counts:
            incorrect_pos += min(guess_counts[color], real_code_counts[color])

    return correct_pos, incorrect_pos  # Return counts of correct positions and colors

def game():
    # Runs the main game loop
    # Print game introduction and instructions
    print(f"Welcome to Mastermind, you have {TRIES} attempts to guess the code...\n")
    print("Guess in increments of 4 for example ('rrrr') or ('GGGG')\n")
    print(f"The valid colors are {COLORS}\n")

    code = generate_code()  # Generate the secret code to be guessed

    # Main game loop for guessing
    for attempts in range(1, TRIES + 1):
        print(f"Tries left: {TRIES - attempts + 1}\n")  # Display remaining tries
        guess = guess_code()  # Get a valid guess from the player
        correct_pos, incorrect_pos = check_code(guess, code)  # Check the guess against the code

        # Check for win condition
        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break  # End the game if the code is correctly guessed

        # Provide feedback on the guess
        print(f"Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}\n")

    else:
        # If the loop completes without a win, the player ran out of tries
        print("You ran out of tries, the code was:", *code)

if __name__ == "__main__":
    game()  # Start the game
