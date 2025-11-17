# Main function to create and display a student
def main():
    student = get_student()  # Get student data from user input
    # If the student's name is Padma, assign them to Ravenclaw
    if student["Name"] == "Padma":
        student["House"] = "Ravenclaw"
    # Print the student's name and house
    print(f"{student['Name']} from {student['House']}")

# Prompt the user for name and house, then return a dictionary
def get_student():
    Name = input("Name: ")     # Ask for the student's name
    House = input("House: ")   # Ask for the student's house
    return {"Name": Name, "House": House}  # Return the student data as a dictionary

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
