# Define a class to represent a wizard's vault with magical currency
class Vault:
    # Initialize the vault with default or specified amounts of galleons, sickles, and knuts
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    # Return a string representation of the vault's contents
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    # Define how to add two Vault objects together
    def __add__(self, other):
        galleons = self.galleons + other.galleons  # Add galleons from both vaults
        sickles = self.sickles + other.sickles    # Add sickles from both vaults
        knuts = self.knuts + other.knuts          # Add knuts from both vaults
        return Vault(galleons, sickles, knuts)     # Return a new Vault with the combined total

# Create a Vault for Potter with specific amounts
potter = Vault(100, 50, 25)
print(potter)  # Print Potter's vault contents

# Create a Vault for Weasley with specific amounts
weasley = Vault(25, 50, 100)
print(weasley)  # Print Weasley's vault contents

# Add both vaults together and print the total
total = potter + weasley
print(f"Total: {total}")
