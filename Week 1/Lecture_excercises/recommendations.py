def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplayer or Single-player? ")

# Two options if choosing Difficult
    if difficulty == "Difficult": # 1st condition
        if players == "Multiplayer":
            recommend("Poker")
        elif players == "Single-player":
            recommend("Mario Bros")
        else:
            print("Enter a valid number of players!")
# Two options if choosing Casual
    elif difficulty == "Casual": # 2nd condition
        if players == "Multiplayer":
            recommend("Call of Duty")
        elif players == "Single-player":
            recommend("Zelda")
        else:
            print("Enter a valid option") # Error message if 2nd condition is not valid
    else:
        print("Enter a valid option") # Error message if 1st condition is not valid

def recommend(game): # Take any condition for "recommend"
    print("You might like", game) # print out a message with the value of any "recommend"

main() # Executes the main function
