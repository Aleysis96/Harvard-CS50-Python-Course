#  implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time.

def main():
    time = input("What time is it? ").strip() # remove spaces
    hour = convert(time)
# Condition the values into when to eat
    if 7 <= hour <= 8:
        print("breakfast time")
    elif 12 <= hour <= 13:
        print("lunch time")
    elif 18 <= hour <= 19:
        print("dinner time")

# Convert the time into float (eg. 7:5 = 7.3), then allows to compare hours easily (eg. 7 < 8)
def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60


if __name__ == "__main__": #
    main()
