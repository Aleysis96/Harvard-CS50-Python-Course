# Define a class to represent a bank account
class Account:
    # Initialize the account with a private balance set to 0
    def __init__(self):
        self._balance = 0

    # Property to access the current balance
    @property
    def balance(self):
        return self._balance

    # Method to deposit money into the account
    def deposit(self, n):
        self._balance += n

    # Method to withdraw money from the account
    def withdraw(self, n):
        self._balance -= n

# Main function to demonstrate account operations
def main():
    account = Account()               # Create a new account
    print("Balance:", account.balance)  # Print initial balance
    account.deposit(100)             # Deposit 100 units
    account.withdraw(50)            # Withdraw 50 units
    print("Balance:", account.balance)  # Print final balance

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
