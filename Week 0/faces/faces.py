# implement a function called convert that accepts a str as input and returns that same input with any :) converted to emojis
def main(): # the program starts here, this is the 1st step the program runs (step 1)
    emoticon = input("Write something with faces: ") # ask user for an emoticon (string)
    emojin = faces(emoticon) # declare the user input as value to be used in def faces
    print(emojin) # print the value already replaced (step 3)

def faces(text): # receives the user input as string (setp 2)
    text = text.replace(":)", "🙂") # look up if the user input has this string and replace it
    text = text.replace(":(", "🙁") # look up if the user input has this string and replace it
    return text

main()

# def main() ask for a value and tells the other function what value to use
# def faces() take the value and use it for the function
# print is the result of the program







