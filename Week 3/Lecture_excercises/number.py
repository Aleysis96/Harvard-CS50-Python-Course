while True: # A loop if user keeps entering an invalid input
    try:
        x = int(input("Enter number: ")) # Ask for a number
    except ValueError:
        print("It's not a number") # if user does not enter a number, print error message
    else:
        break # As long user enter a valid integer, end the loop and print the result

print(f"x is {x}")

# You can use the break after the input, if the user enters a correct input you can break it right there instead using else
