import re

email = input("You email address? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE): # a short version
    print("Valid")
elif re.search(r"^[a-zA-Z0-9_\.]+@[a-zA-Z0-9_\.]+\.(com|gov|net)$", email, re.IGNORECASE): # works the same but specifying the valid characters
    print("Valid")
else:
    print("Invalid")


# re library expressions

# . any character except a newline
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetition
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end of the string or before a newline at the end of the string
# \ is meant to use a string literally (i.e \. means that . has to be enter literally)
# [] set of characters
# [^] a character you want to exclude
# \w any word character as well as numbers and underscore
# \d decimal digit
# \D not decimal digit
# \s whitespace characters
# \S not whitespace character
# \W not a word character
# A|B either one character or B other character
# (...) a group dividing them with |
# (?:...) non-capturing version
# re.IGNORECASE ignore either uppercase or lowercase
# re.search
# re.match
# re.fullmatch
# re.sub substitute a string to another string
