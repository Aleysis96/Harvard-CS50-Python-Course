#  Implement a program that prompts the user for an email address via input and then prints Valid or Invalid

from validator_collection import validators, errors

email = input("What's your email address? ")

try:
    validated_email = validators.email(email)
    print("Valid")
except errors.InvalidEmailError:
    print("Invalid")
