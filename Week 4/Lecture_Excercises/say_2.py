import sys # Imports the sys module to access command-line arguments

from sayings import goodbye # import the functions made by myself in other program

if len(sys.argv) == 2: # If exactly one argument is passed after the script name
                       # Note: the 1 argument is always the name of the file
    goodbye(sys.argv[1]) # [] is part of a list, so 1 is the first value entered on the list, wich is what the user typed

