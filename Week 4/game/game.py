# implement a guessing program

import random # Imports the random module to generate a random number

while True: # Loop until the user enters a valid positive level
    number = input("Level: ") # Prompt the user to enter a difficulty level
    if number.isdigit(): # Check if the input is a digit
         number = int(number) # Convert the input to an integer
         if number > 0: # Ensure the level is a positive number
                secret = random.randint(1, number) # Generate a random number between 1 and the chosen level
                guessing = input("Guess: ") # Prompt the user to guess the number
                if guessing.isdigit(): # Check if the guess is a digit
                    guessing = int(guessing) # Convert the guess to an integer
                    if guessing == secret: # Compare the guess to the secret number
                        print("Just right!")
                        break # Exit the loop
                    elif secret < guessing:
                        print("Too large!") # Guess is too high
                    elif secret > guessing:
                        print("Too small!") # Guess is too low





# random.randint(int1, int2) # print a random numbers between a range (0, 10)
