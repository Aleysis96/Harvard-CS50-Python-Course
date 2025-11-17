# Define a function that returns a string of "meow" repeated n times, each on a new line
def meow(n: int) -> str:
    """
    Meow n time.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: if n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

# Prompt the user to enter a number and convert it to an integer
number: int = int(input("Number: "))

# Call the meow function with the user's input and store the result
meows: str = meow(number)

# Print the result without adding an extra newline at the end
print(meows, end="")
