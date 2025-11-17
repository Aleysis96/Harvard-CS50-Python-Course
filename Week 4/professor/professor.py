 # implement a program to solve math problems

import random

def main():
    level = get_level() # call get_level function
    score = 0 # Initialize score

    for _ in range(10):
        x, y = generate_integer(level) # Generate two random integers based on level
        correct = x + y # Calculate the correct answer
        tries = 0 # Track number of attempts
        while tries < 3: # Allow up to 3 attempts to solve the problem
            try:
                answer = int(input(f"{x} + {y} = ")) # Prompt user for answer
                if answer == correct:
                    score += 1 # Increase score if correct
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            tries += 1
        if tries == 3:
            print(f"Answer: {correct}") # If user fails after 3 attempts, show the correct answer

    print("Score:", score)

def get_level(): # Function to prompt and validate difficulty level
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)

def generate_integer(level): # Function to generate two random integers based on difficulty level
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9) # Single-digit numbers
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99) # Two-digit numbers
    elif level == 3:
        return random.randint(100, 999), random.randint(100, 999) # Three-digit numbers

if __name__ == "__main__":
    main()
