# Tip calculator (Assuming that the user will input values in the expected formats like "$50.00" and "15%".)
def main():
    dollars = dollars_to_float(input("How much was the meal? ")) # Ask for meal cost in format like "$50.00"
    percent = percent_to_float(input("What percentage would you like to tip? ")) # # Ask for tip percentage like "15%"
    tip = dollars * percent / 100 # multiply the values and divided by 100 to obtain the decimal value
    print(f"Leave ${tip:.2f}") # result of the calculation

def dollars_to_float(dollars):
    dollars = dollars.replace("$","") # replace the (expected) $ to a blank string
    dollars = float(dollars) # use the value of the replacament and convert it to decimal
    return dollars # Return the numeric value to be used in calculations

def percent_to_float(percent):
    percent = percent.replace("%","") # replace the (expected) % to a blank string
    percent = float(percent) # use the value of the replacament and convert it to decimal
    return percent # Return the numeric value to be used in calculations

main()
