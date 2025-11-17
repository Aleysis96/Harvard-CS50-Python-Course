# Main function to prompt user input and greet them
def main():
    # Ask the user to enter their name
    name = input("Your name? ")

    # Print a personalized greeting
    print(hello(name))

# Function to return a greeting message
def hello(to="world"):
    # Return a formatted greeting string
    return f"hello, {to}"

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
