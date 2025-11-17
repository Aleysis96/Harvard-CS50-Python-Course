# Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels(A,E,I,O,U) omitted.

vowels = ["A","E","I","O","U","a","e","i","o","u"] # a list of vowels in upper and lower case
enter = input("Input: ")

for vow in vowels: # loops every value on the list
    if vow in enter: # if the value from the list is in user's input...
        enter = enter.replace(vow, "") # replace the value on the list to a blank ""

print("Output:", enter) # shows the result on enter in the condition



