WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7} # Dictionary of valid words and their point values

def main(): # Welcome message and display available letters
    print("Welcome To Bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0: # Loop continues as long as there are words left in the dictionary
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ").upper() # upper case user's input in case user inputs in lower case

        # TODO: Check if guess in dictionary
        if guess == "GRAPHIC": # Special condition: if the guess is "GRAPHIC", clear all words and declare victory
            WORDS.clear()
            print("You've won!")
        if guess in WORDS.keys(): # If the guessed word is in the dictionary, award points and remove the word
            points = WORDS.pop(guess)
            print(f"Good job! You scored {points} points.") # Final message after all words are guessed or cleared

    print("Good Job!")

main() # Call the main function
