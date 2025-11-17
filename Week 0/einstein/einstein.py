#  implement a program in Python that prompts the user for mass as an integer (in kilograms)
# and then outputs the equivalent number of Joules as an integer.
def main():
    value = int(input("Type a whole number ")) # ask the user for a whole value
    result = albert(value) # use that value to send it to the other function
    print(result) # shows the result

def albert (number): # number itself is the value given by user in previous function
    number = number*90000000000000000 # take the value and multiply it
    return number # take the result of the calculation and send it to main function to use it


main()
