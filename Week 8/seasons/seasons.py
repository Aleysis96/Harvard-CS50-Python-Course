# implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes,
# rounded to the nearest integer, using English words instead of numerals

from datetime import date
import inflect
import sys

# Create an inflect engine to convert numbers to words
p = inflect.engine()

# Main function to prompt user input and display age in minutes
def main():
    # Ask the user to enter their date of birth in ISO format (YYYY-MM-DD)
    birth = input("Date of Birth: ")

    # Print the result of the get_minutes function
    print(get_minutes(birth))

# Function to calculate the number of minutes since birth and return it in words
def get_minutes(birth):
    try:
        # Convert the input string to a date object
        time = date.fromisoformat(birth)
    except ValueError:
        # If the input is not a valid date, print an error and exit
        print("Invalid date")
        sys.exit(1)

    # Get today's date
    current = date.today()

    # Calculate the number of days between birth and today
    days = (current - time).days

    # Convert days to minutes
    minutes = days * 24 * 60

    # Convert the number of minutes to words (without "and")
    result = p.number_to_words(minutes, andword='')

    # Return the result with the first letter capitalized
    return f"{result.capitalize()} minutes"

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
