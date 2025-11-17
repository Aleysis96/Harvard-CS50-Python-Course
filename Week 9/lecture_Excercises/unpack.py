# Define a function to convert wizarding currency to total knuts
def total(galleons, sickles, knuts):
    # 1 Galleon = 17 Sickles, 1 Sickle = 29 Knuts
    return (galleons * 17 + sickles) * 29 + knuts

# Dictionary representing the amount of each coin
coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# Unpack the dictionary into the function and print the total in knuts
print(total(**coins), "Knuts")
