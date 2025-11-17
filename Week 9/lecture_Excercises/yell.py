# Main function to demonstrate yelling behavior
def main():
    yell("this is cs50")  # Pass a single string to the yell function

# Function that prints each word in uppercase
def yell(*words):
    # Convert each word to uppercase
    uppercased = [word.upper() for word in words]
    # Print the uppercase words separated by spaces
    print(*uppercased)

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
