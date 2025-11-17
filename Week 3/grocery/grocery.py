# implement a program that prompts the user for items, one per line, until the user inputs control-d
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item
# Prefixing each line with the number of times the user inputted that item.

Grocery = {} # Initialize an empty dictionary to store item counts

while True:
    try:
        list = input().upper() # uppercase all inputs

        if list in Grocery: # If the item already exists in the dictionary, increment its count
             Grocery[list] += 1 # since the loop still running, the item added is counted in condition
        else:
             Grocery[list] = 1 # If it's a new item, add it to the dictionary with a count of 1
    except EOFError:
            for name in sorted(Grocery): # when the user presses Ctrl+D (EOF), sort the items alphabetically
                print(f"{Grocery[name]} {name}") # count how many times that item was entered
            exit()
