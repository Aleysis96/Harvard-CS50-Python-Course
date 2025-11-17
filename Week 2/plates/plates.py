# Main function to prompt user input and validate the plate
def main():
    # Ask the user to enter a plate, remove surrounding spaces, and convert to uppercase
    plate = input("Plate: ").strip().upper()

    # Check if the plate is valid and print the result
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Function to validate the plate according to specific rules
def is_valid(s):
    # Rule 1: Plate must be between 2 and 6 characters long
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: The first two characters must be letters
    if not s[0:2].isalpha():
        return False

    # Rule 3: All characters must be alphanumeric (letters or digits)
    if not s.isalnum():
        return False

    # Rule 4: If the plate contains digits, they must appear at the end
    if any(char.isdigit() for char in s):
        # Find the index of the first digit
        first_digit_index = min((i for i in range(len(s)) if s[i].isdigit()), default=None)

        if first_digit_index is not None:
            # Rule 5: The first digit cannot be zero
            if s[first_digit_index] == '0':
                return False

            # Rule 6: All characters after the first digit must be digits
            if not s[first_digit_index:].isdigit():
                return False

    # If all rules pass, the plate is valid
    return True

# Run the main function than runs all functions within
main()

# Note: s.startswith("0") is not used here, but could be relevant in other validations
