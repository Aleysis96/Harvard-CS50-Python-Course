# Define a class to represent a student
class Student:
    # Initialize student attributes using property setters
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # Return a string representation of the student
    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for the name attribute
    @property
    def name(self):
        return self._name

    # Setter for the name attribute with validation
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")  # Raise error if name is empty
        self._name = name

    # Getter for the house attribute
    @property
    def house(self):
        return self._house

    # Setter for the house attribute with validation
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")  # Raise error if house is not valid
        self._house = house

# Main function to create and display a student
def main():
    student = get_student()  # Get student data from user input
    print(student)           # Print the student's details

# Prompt the user for name and house, then return a Student object
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
