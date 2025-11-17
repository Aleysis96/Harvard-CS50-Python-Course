fruits = {
    "Apple": "130",
    "Avocado": "50",
    "Sweet Cherries": "100",
    "Kiwifruit": "90",
    "Pear": "100"
}

item = input("Item: ").strip().title()  # Capitalize input: "apple" → "Apple"

if item in fruits:
    print("Calories:", fruits[item])
else:
    print("Item not found.")

# in dictionaries, when open fruits[] it takes the value from the key, eg: Apple[130]
# we can just use a condition if to match the value with the key instead
