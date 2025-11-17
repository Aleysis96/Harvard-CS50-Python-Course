import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua", "+52": "Mexico"}

def main():
    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        country_code = match.group("country_code")
        print(f"Call from {locations[country_code]}")
    else:
        print("Invalid")

main()
