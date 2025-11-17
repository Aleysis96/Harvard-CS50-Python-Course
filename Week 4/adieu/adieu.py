# implement a program that prompts the user for names, one per line, until the user inputs control-d.

import inflect # Imports the inflect library to handle proper English grammar

adieu = [] # Initializes an empty list to store names entered by the user
adios = inflect.engine() # Starts the engine instance to format the final output (as per doc from the library)

while True: # Continuously prompts the user for names until an EOF signal (Ctrl+D) is received
    try:
        bye = input("Name: ") # Asks the user to input a name
        adieu.append(bye) # Adds the entered name to the list

    except EOFError:
        print("") # Prints a blank line for visual separation
        print(f"Adieu, adieu, to {adios.join(adieu)}") # Uses inflect to join the list of names into a grammatically correct phrase
        exit()

