# Function to assign a dollar value based on the greeting
def value(greeting):
    # Convert the greeting to lowercase for consistent comparison
    greeting = greeting.lower()

    # If the greeting starts with "hello", return 0
    if greeting.startswith("hello"):
        return 0
    # If it starts with any other word beginning with "h", return 20
    elif greeting.startswith("h"):
        return 20
    # Otherwise, return 100
    else:
        return 100

# Main function to prompt user input and display the result
def main():
    # Ask the user to enter a greeting
    user_input = input("Greeting: ")

    # Print the dollar value based on the greeting
    print(f"${value(user_input)}")

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
