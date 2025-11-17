import sys  # Imports the sys module to access command-line arguments

if len(sys.argv) < 2:  # Checks if no argument was passed after the script name
    print("Write some after python file name please >.< ")
elif (
    len(sys.argv) > 2
):  # Checks if more than one argument was passed (e.g., multiple words without quotes)
    print("Too many names D: ")
    print("You can use quotes between if want to type full name :)")
else:
    print("Hello :D", sys.argv[1])  # If exactly one argument is passed, greet the user
