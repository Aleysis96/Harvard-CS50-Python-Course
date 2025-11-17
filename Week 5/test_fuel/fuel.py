# Main function to prompt user input and display fuel gauge status
def main():
    while True:
        try:
            # Ask the user to enter a fraction (e.g., "3/4")
            fraction = input("Fraction: ")

            # Convert the fraction to a percentage
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            # If input is invalid, retry without showing an error
            pass

    # Print the gauge reading based on the percentage
    print(gauge(percentage))

# Function to convert a fraction string to a percentage
def convert(fraction):
    # Split the input string and convert to integers
    numerator, denominator = map(int, fraction.split("/"))

    # Raise an error if denominator is zero or numerator is negative
    if denominator == 0 or numerator < 0:
        raise ZeroDivisionError

    # Calculate the percentage
    result = numerator / denominator * 100

    # Raise an error if the result exceeds 100%
    if result > 100:
        raise ValueError

    return result

# Function to return a fuel gauge reading based on percentage
def gauge(percentage):
    if percentage < 2:
        return "E"  # Empty
    elif percentage >= 99:
        return "F"  # Full
    else:
        return f"{round(percentage)}%"  # Rounded percentage

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
