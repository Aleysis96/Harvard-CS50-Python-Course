distances = { # keys and values
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New horizons": 58,
    "Pioneer 11": 44
}

def main():
    for distance in distances.values(): # we named the loop distance and we take the values from the dictionary
        print(f"{distance} AU is {convert(distance)} Meters") # Concatenate with f and we take the results from the loop and convert function
        # the print line is a whole concatenate line, we using variables o functions names to put it all together.
        
def convert(au): # we defined convert as "au"
    return au * 149597870700 # we multiply the value of convert with that number

main()
