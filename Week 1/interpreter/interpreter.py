# implement a program that prompts the user for an arithmetic expression
# and then calculates and outputs the result as a floating-point value formatted to one decimal place

def main():
    Exp = input("Expression: ") # user has to input an space between the 2 values, otherwise it'll failed
    x, y, z = Exp.split(" ")
# Convert each variable to its specific format
    x = float(x)
    y = str(y)
    z = float(z)
# Conditioned each string to an operator and calculates
    if y == "+":
        print(round(x+z,2))
    elif y == "-":
        print(round(x-z,2))
    elif y == "*":
        print(round(x*z,2))
    elif y == "/":
        print(round(x/z,2))
    else:
        print("Invalid input") # if user inputs a non existing operator


main()
