# With boolean expressions and less lines of codes

# Boleean expression is used to short the error message if any of the first conditions is true
def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid option")
        return

    players = input("Multiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single-player"):
        print("Enter a valid option")
        return

# booleean expression is used to short the conditions into one line
    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Mario bros")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Call of Duty")
    else:
        recommend("Zelda")

def recommend(game): # Take any condition for "recommend"
    print("You might like", game) # print out a message with the value of any "recommend"

main()
# line 28 executes the "def main" function
# def main() executes "def recommend" function
# in the end, line 28 "main()" executes the whole program
