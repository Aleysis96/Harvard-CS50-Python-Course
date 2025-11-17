# implement a function called count that expects a line of text as input as a str and returns,
# as an int, the number of times that “um” appears in that text

import re

# Main function to prompt user input and count occurrences of "um"
def main():
    # Ask the user to enter a text and print the count of "um"
    print(count(input("Text: ")))

# Function to count standalone occurrences of "um" (case-insensitive)
def count(s):
    # Regular expression pattern to match the word "um" as a whole word
    pattern = r'\bum\b'

    # Find all matches of "um" in the input string, ignoring case
    match = re.findall(pattern, s, re.IGNORECASE)

    # Return the number of matches found
    if match:
        return len(match)
    else:
        return 0

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
