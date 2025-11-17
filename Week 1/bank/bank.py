# implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100

def main():
    greeting = input("Greeting: ").strip().lower() # we remove spaces and capitalized letters
    if greeting == "hello" or greeting == "hello there" or greeting == "hello, newman": # we have to specify the exact input after removing spaces and capitalized letters
        print("$0")
    elif greeting.startswith("h") and not greeting.startswith("hello"):
        print("$20")
    else:
        print("$100")


main()
