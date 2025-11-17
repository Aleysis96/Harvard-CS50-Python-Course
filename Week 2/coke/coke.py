def main():
    amount_due = 50

    while amount_due > 0:
        print("Amount Due:", amount_due) # shows the amount due
        coin = input("Insert Coin: ") # ask user for a coin

        if coin.isdigit(): # Check if the input is positive and a number
            coin = int(coin) # convert the input into a number(integer)
            if coin in [25, 10, 5]: # a list of valid inputs
                amount_due -= coin # subtract the input value from the original amount
            else:
                print("Invalid coin. Accepted coins are: 25, 10, 5") # if input is not valid within the list
        else:
            print("Invalid input. Please enter a number.") # if the original input is negative or a string, shows the message

    print("Change Owed:", abs(amount_due)) # remove negative sign if there is

main()
