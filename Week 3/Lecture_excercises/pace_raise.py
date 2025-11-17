def main():
    pace = get_pace(miles=26.2, minutes=0)
    print(f"You need to run each mile in {round(pace, 2)} minutes.") # f is use to concatenate strings with values from the program

def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Minutes must be greater than 0.") # prints a message error within the terminal
    return minutes / miles

main()

# this is a prototype to shows how to raise error messages
