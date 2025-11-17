from helpers import get_words, save_counts # Import helper functions from external module

def main():
    words = get_words("address.txt") # Load words from the file "address.txt"
    lowercase_words = [word.lower() for word in words if len(word) > 4] # Create a list of lowercase words, filtering out any with 4 or fewer characters

    # Count how many times each word appears in the filtered list
    # Dictionary comprehension: each key is a word, each value is its frequency
    counts = {words: lowercase_words.count(word) for word in lowercase_words}

    save_counts(counts) # Save the word counts using a helper function (e.g., to a file or database)


main() # Run the main function to execute the program
