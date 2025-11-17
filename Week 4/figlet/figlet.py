#  implement a program FIGlet

from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # Case: zero arguments (just the script name)
    if len(sys.argv) == 1:
        font = random.choice(fonts)
        figlet.setFont(font=font)

    # Case: two arguments (script name + 2 args)
    elif len(sys.argv) == 3:
        option, font_name = sys.argv[1], sys.argv[2]

        # Validate option and font name
        if option not in ["-f", "--font"] or font_name not in fonts:
            sys.exit("Invalid usage")

        figlet.setFont(font=font_name)

    # Any other case is invalid
    else:
        sys.exit("Invalid usage")

    # Prompt user for input and render text
    text = input("Input: ")
    print(figlet.renderText(text))

if __name__ == "__main__":
    main()
