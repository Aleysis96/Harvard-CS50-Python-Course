# Main function to prompt user input and print sheep patterns
def main():
    n = int(input("N: "))        # Ask the user for a number
    for s in sheep(n):           # Iterate over the generator returned by sheep()
        print(s)                 # Print each sheep pattern

# Generator function that yields a growing number of sheep emojis
def sheep(n):
    for i in range(n):          # Loop from 0 to n-1
        yield "🐑" * i           # Yield a string with i sheep emojis

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
