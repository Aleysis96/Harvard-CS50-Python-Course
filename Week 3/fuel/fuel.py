#  implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is a positive integer,
# and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank.

def main():
    while True:
        try:
            tank = input("Fraction: ").split("/") # ask for fraction and splits the "/" to leave just the numbers
            numerator = int(tank[0]) # convert the first string into a integer
            denominator = int(tank[1]) # convert the second string into a integer
            if not denominator == 0 and not numerator < 0: # as long is not dividing to zero and use negatives
                result = numerator / denominator * 100 # formula to get percentaje of a fraction
                if not result > 100: # as long result is not over 100
                    return result # return result to use it in next function
        except ValueError:
                    pass # do not shows error message, instead re-ask again the main question until the condition is true

def get_result(result):
    if result < 2: # if results is less than 2, prints empty
        print("E")
    elif result >= 99: # if result is more than 99 but no more than 100, prints full
        print("F")
    else:
        print(f"{round(result)}%")

result = main() # declare main function as the result from input
get_result(result) # gives to main function the value of the input


# here's another version of the program with just using 1 main function
#def main():
#    while True:
#        try:
#            tank = input("Fraction: ").split("/")
#            numerator = int(tank[0])
#            denominator = int(tank[1])
#            if not denominator == 0 and not numerator < 0:
#                result = numerator / denominator * 100
#                if not result > 100:
#                    if result < 2:
#                        print("E")
#                    elif result >= 99:
#                        print("F")
#                    else:
#                        print(f"{round(result)}%")
#                    break
#        except ValueError:
#            pass
# main()
