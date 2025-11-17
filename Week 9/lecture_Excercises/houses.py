# List of student dictionaries with name and house information
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# Create an empty set to store unique house names
houses = set()

# Loop through each student and add their house to the set
for student in students:
    houses.add(student["house"])

# Sort the set of houses alphabetically and print each one
for house in sorted(houses):
    print(house)
