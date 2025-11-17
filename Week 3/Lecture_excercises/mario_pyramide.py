# Main function to prompt user input and build the pyramid
def main():
    # Ask the user to enter the pyramid height and convert it to an integer
    height = int(input("Height: "))

    # Call the pyramid function with the given height
    pyramid(height)

# Function to print a left-aligned pyramid of '#' characters
def pyramid(n):
    # Loop from 0 to n-1 to build each row
    for i in range(n):
        # Print a row with i number of '#' characters
        print("#" * i)

# Run the main function
main()
