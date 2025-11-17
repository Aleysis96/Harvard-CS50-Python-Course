# Main function to start the program
def main():
    # Call the function to print a square of size 3
    print_square(3)

# Function to print a square of given size
def print_square(size):
    # Loop through each row of the square
    for i in range(size):
        # Print a single row of the square
        print_row(size)

# Function to print a row of given width using '#'
def print_row(width):
    print("#" * width)

# Run the main function
main()
