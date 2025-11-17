def main():
    number = get_number() # declare the variables as the value from get_number function
    meow(number) # meow is the number of times get_number was declared

def get_number():
    while True:
        n = int(input("number: ")) # asking user a number
        if n > 0:
            break # as long the user input is greater than 0, don't ask again
    return n

def meow(n):
    for i in range(n): # takes the value of the user input as range
        print("meow") # print "meow"

main() # call the function
