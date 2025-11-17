# Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels(A,E,I,O,U) omitted.

# Main function to prompt user input and display the shortened word
def main():
    # Ask the user to enter a word and convert it to lowercase
    word = input("Input: ").lower()

    # Print the word with vowels removed
    print("Output:", shorten(word))

# Function to remove all vowels from the input word
def shorten(word):
    # List of vowels to remove (both uppercase and lowercase)
    vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

    # Replace each vowel in the word with an empty string
    for vow in vowel:
        word = word.replace(vow, "")

    # Return the shortened word
    return word

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
