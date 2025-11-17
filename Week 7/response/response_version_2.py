# if want specific email address using different variables to validate each email address.

from validator_collection import validators

email = input("Email: ")

email_address_1 = validators.email('adidas_cardona@hotmail.com')
email_address_2 = validators.email('alesis096@gmail.com')
email_address_3 = validators.email('alexis.cardona@tp.com')

if email == email_address_1 or email == email_address_2 or email == email_address_3:
    print("Valid")
else:
    print("Invalid")
