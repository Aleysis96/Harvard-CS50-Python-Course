# List of student dictionaries with name and house information
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# Function to check if a student belongs to Gryffindor
def is_gryffindor(s):
    return s["house"] == "Gryffindor"

# Filter the list to include only Gryffindor students
gryffindors = filter(is_gryffindor, students)

# Sort the Gryffindor students by name and print each name
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
