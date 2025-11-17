# Define a class to represent a student
class Student:
    # Initialize student attributes: name and house
    def __init__(self, name, house):
        self.name = name
        self.house = house

    # Return a string representation of the student
    def __str__(self):
        return f"{self.name} from {self.house}"

    # Class method to prompt user input and create a Student object
    @classmethod
    def get(cls):
        name = input("Name: ")       # Ask for the student's name
        house = input("House: ")     # Ask for the student's house
        return cls(name, house)      # Return a new Student instance

# Main function to create and display a student
def main():
    student = Student.get()         # Create a student from user input
    print(student)                  # Print the student's details

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
