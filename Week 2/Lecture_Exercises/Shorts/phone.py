def main():
    phone = input("Type you phone: ").strip() # ask user for number and removes spaces
    phone_no_spaces = phone.replace(" ", "").replace("-", "") # Count characters without spaces and special character
    if len(phone_no_spaces) >= 8: # if number entered has more than 8 characters, then...
        print("Code sent to:", "*******", phone_no_spaces[-4:])  # Show masked code and last 4 digits
    else:
        print("Incorrect number")  # Too short or invalid input

main() # Call the main function to execute the program
