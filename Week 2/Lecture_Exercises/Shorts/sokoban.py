def main():
    history = [] # a list is adding based on the user's input

    while True:
        action = input("Action: ") # Ask user for a move

        if action == "Undo": # If user inputs "Undo", remove the last input of the user
            undone = history.pop()
            print(f"Undone: {undone}") # prints the move it was removed
        elif action == "Restart":
            history.clear() # if user inputs "Restart", removes all user inputs ever
        else:
            history.append(action) # if user never inputs "Undo" or "Restart", every user's move is added in the main list

        print(history) # prints all list values

main() # Calls the main function
