# Import the sys module to access command-line arguments
import sys

# Check if no additional arguments were provided
if len(sys.argv) == 1:
    print("meow")

# Check if the user provided the "-n" flag followed by a number
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])  # Convert the second argument to an integer
    for _ in range(n):    # Print "meow" n times
        print("meow")

# Handle incorrect usage by showing a usage message
else:
    print("usage: meows.py")
