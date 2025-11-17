# Implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything

def main():
    Answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower() # we remove spaces and capitalized letters
    if Answer == "42" or Answer == "forty-two" or Answer == "forty two":
        print("Yes")
    else:
        print("No")


main() # Calls the function

