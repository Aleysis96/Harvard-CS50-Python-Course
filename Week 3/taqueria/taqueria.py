Taqueria = { # dict of dishes with keys and values
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00

}

total_of_orders = 0 # Initialize the total cost of all ordered items
Order = "" # Variable to store the user's input (menu item)

while True: # as long eveything within the condition, keeps running
        try:
            Order = input("Item: ").title() # regardless of the user input, it will always be title case the first letter (to match the keys on dict)
            if Order in Taqueria: # Check if the entered item exists in the Taqueria menu
                total = float(Taqueria[Order]) # Retrieve the value of the order (from dict) and convert it to float
                total_of_orders += total # add the order's price to the running total of order variable
                print(f"Total: ${total_of_orders:.2f}") # ':.2f' prints the total with two decimals, regardless if its only 0.00
        except EOFError:
            exit() # If the user presses Ctrl+D (EOF), exit the program on same prompt line (as requested by problem)
                   # if we intend to jump the line, just add ("")

# we can use a function 'def main()' by just adding the two variables of 'total orders' and 'Order' inside the function
# eg..
# def main():
#   total_of_items = 0
#   Order = ""
#   while True:
#       .....
#       .....

# main()
