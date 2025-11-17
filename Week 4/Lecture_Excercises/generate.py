import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)


# random.randint(int1, int2) # print a random numbers between a range (0, 10)
# random.choice(["", ""]) # choice between two or more values
# random.shuffle(list) # shuffle random values from a list
# you can either import the function or just import the whole module but has to call the function everytime
