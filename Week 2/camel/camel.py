# Prompt the user to enter a camelCase string
camel = input("camelCase: ")

# Initialize an empty string to build the snake_case version
case = ""

# Loop through each character in the input string
for snake in camel:
    # If the character is uppercase, add an underscore and convert it to lowercase
    if snake.isupper():
        case += "_" + snake.lower()
    # If the character is lowercase, add it as is
    else:
        case += snake

# Print the converted snake_case string
print("snake_case:", case)
