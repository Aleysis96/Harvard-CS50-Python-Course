# another version if you want to just validate specifics email address by using a list.

from validator_collection import validators, errors

emails = ['malan@harvard.edu', 'carter@harvard.edu']
email = input("Email: ")

try:
    validated_email = validators.email(email)
    if validated_email in emails:
        print("Valid")
except errors.InvalidEmailError:
    print("Invalid")
