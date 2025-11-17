# Main function to prompt user input and convert AU to meters
def main():
    while True:
        # Ask the user to enter a value in astronomical units (AU)
        au = input("AU: ")
        try:
            # Try converting the input to a float
            au = float(au)
            break
        except ValueError:
            # If conversion fails, prompt again
            continue

    # Print the converted value in meters
    print(f"{au} AU is {convert(au)} m")

# Function to convert AU to meters
def convert(au):
    # Ensure the input is a number (int or float)
    if not isinstance(au, (int, float)):
        raise TypeError("au must be an int or float")

    # Multiply AU by the standard conversion factor to meters
    return au * 149597870700

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()

