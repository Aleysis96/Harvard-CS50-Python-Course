import random # Imports the random module to enable random selection functions

cards = ["jack", "queen", "king"]

def main():
    random.seed(1) # Sets the random seed to ensure reproducible results
    print(random.choices(cards, weights=[75, 20, 5], k=2)) # Selects 2 cards (keys) from the list using weighted probabilities
    # "jack" has a 75% chance, "queen" 20%, and "king" 5%


main()
