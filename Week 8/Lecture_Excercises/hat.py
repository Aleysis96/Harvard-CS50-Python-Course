# Import the random module to enable random selection
import random

# Define a class called Hat
class Hat:
    # Class variable containing the list of Hogwarts houses
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # Class method to randomly assign a house to a given name
    @classmethod
    def sort(cls, name):
        # Print the name and the randomly chosen house
        print(name, "is in", random.choice(cls.houses))

# Prompt the user to enter a name and sort them into a house
Hat.sort(input(("Name: ")))
