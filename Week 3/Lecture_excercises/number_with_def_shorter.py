def main():
    x = get_num("Enter number: ") # define the parameter to the get_num function
    print(f"x is {x}")

def get_num(prompt): # define the parameter to use it on an input
    while True:
        try:
            return int(input(prompt)) # takes the parameter of the main function
        except ValueError:
            pass # except of printing an error message, just ask again the main question

main()
