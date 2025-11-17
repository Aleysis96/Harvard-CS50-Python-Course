# implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str,
# converting any codes (or aliases) therein to their corresponding emoji.

import emoji # Imports the emoji library to convert emoji aliases into actual emoji characters

def main():
    emoticon = input("Input: ") # Ask user for an written emoji
    print(emoji.emojize(f"Output: {emoticon}", language='alias')) # Converts the alias into an actual emoji and prints it


main()
