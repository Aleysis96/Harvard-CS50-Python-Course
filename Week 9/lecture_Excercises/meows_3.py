# Import the argparse module to handle command-line arguments
import argparse

# Create an ArgumentParser object with a description of the program
parser = argparse.ArgumentParser(description="Meow like a cat")

# Add an optional argument -n to specify how many times to meow
parser.add_argument("-n", default=1, help="Number of times to meow", type=int)

# Parse the command-line arguments and store them in args
args = parser.parse_args()

# Print "meow" the specified number of times
for _ in range(int(args.n)):
    print("meow")
