distances = { # keys and values
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80",
    "New horizons": "58",
    "Pioneer 11": "44"
}

def main():
    spacecraft = input("Enter a spacecraft: ")

    try:
        au = float(distances[spacecraft]) # converts into a digit the values from dictionary
    except KeyError:
        print(f"'{spacecraft}' is not in dictionary") # if user inputs a non existing key from dictionary
        return
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to meters") # if values from dictionary are strings rather than numbers
        return
    m = convert(au) # take the value from from input then pass it to below function and then is return it back to main function
    print(f"{m} m away")

def convert(au): # we defined convert as "au"
    return au * 149597870700 # we multiply the value of convert with that number

main()
