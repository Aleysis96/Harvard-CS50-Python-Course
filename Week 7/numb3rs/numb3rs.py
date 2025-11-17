# Implement a function called validate that expects an IPv4 address as input as a str and then returns True or False

import re

# Main function to prompt user input and validate the IPv4 address
def main():
    # Ask the user to enter an IPv4 address and print whether it's valid
    print(validate(input("IPv4 Address: ")))

# Function to validate an IPv4 address using a regular expression
def validate(ip):
    # Regular expression pattern to match valid IPv4 addresses
    pattern = r"^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"

    # Search for a match using the pattern
    match = re.search(pattern, ip)

    # Return "True" if the address is valid, otherwise "False"
    if match:
        return "True"
    else:
        return "False"

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
