# implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit

fruits = {
    "Apple": "130",
    "Avocado": "50",
    "Sweet Cherries": "100", # a dictionary with its keys and values
    "Kiwifruit": "90",
    "Pear": "100",
}

Item = input("Item: ").strip().title() # ask for input, remove spaces and capitalize the first letter of every input

for key, value in fruits.items():
    if Item == key: # Check if the user's input matches the current key
        print("Calories:", value) # If it matches, print the corresponding calorie value



# in dictionaries, when open fruits[] it takes the value from the key, eg: Apple[130]
# we can just use a condition if to match the value with the key instead
