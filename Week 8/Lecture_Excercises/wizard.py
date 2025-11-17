# Define a base class for all wizards
class Wizard:
    # Initialize the wizard with a name, raising an error if missing
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

# Define a subclass for students, inheriting from Wizard
class Student(Wizard):
    # Initialize the student with a name and house
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

# Define a subclass for professors, inheriting from Wizard
class Professor(Wizard):
    # Initialize the professor with a name and subject
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

# Create a Wizard instance
wizard = Wizard("Albus")

# Create a Student instance
student = Student("Harry", "Gryffindor")

# Create a Professor instance
professor = Professor("Severus", "Defense")
