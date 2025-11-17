# Define a class to represent a package
class Package:
    # Initialize package attributes: number, sender, recipient, and weight
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    # Return a string representation of the package
    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight}kg"

    # Calculate the shipping cost based on weight and cost per kilogram
    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg

# Main function to create and display package information
def main():
    # Create a list of package objects with sample data
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight=5)
    ]
    # Print each package's details and calculated cost
    for package in packages:
        print(f"{package}, cost ${package.calculate_cost(cost_per_kg=2)}")

# Run the main function
main()
