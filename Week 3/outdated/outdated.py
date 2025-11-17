from datetime import datetime # importing and using python method to formate a string to date

# List of valid month names
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")

    try:
        # First check all value in the list
        # Then check if input contains a month name from the list already checked (e.g., "September")
        if any(month in date for month in months):
            # Try parsing format like "September 8, 1636"
            format_date = datetime.strptime(date, "%B %d, %Y") # %B represents the full month name in python datetime method
        else:
            # Try parsing format like "9/8/1636"
            format_date = datetime.strptime(date, "%m/%d/%Y")

        # Format and print as YYYY-MM-DD
        print(format_date.strftime("%Y-%m-%d"))
        break  # Exit loop after successful parsing

    except ValueError:
        # Invalid format, prompt again
        pass


# to change a string to a date format, need to always import datetime
