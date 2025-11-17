def main(): # List of names to receive the invitation
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in names: # declare a name for the loop, as declaring a variable but in here using the loop sintax
        print(write_letter(name, "Princess Peach")) # Loop through each name and print a personalized letter


# Function that generates a formatted invitation letter
def write_letter(receiver, sender): # Takes two arguments: receiver (who gets the letter) and sender (who sends it)
# receiver is the 1st argument in print from main function and sender is the 2nd argument in print from main function
    return f"""
    + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ +

       Dear {receiver},

       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {sender}

    + ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ +
    """
# allows multiline formats text with option to include variables {} and also keeping the format as exactly as written on the output

main() # Call the main function to execute the program

# Extras tips:

# f"..." → single-line f-string
# """...""" → multiline string without formatting
# f"""...""" → multiline f-string keeping formatting
