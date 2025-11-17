# implement a function called convert that expects a str in any of the 12-hour formats below
# and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).

import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression to match all four valid formats
    pattern = r'^(\d{1,2})(?::(\d{2}))?\s(AM|PM)\sto\s(\d{1,2})(?::(\d{2}))?\s(AM|PM)$'
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid format")

    h1, m1, p1, h2, m2, p2 = match.groups()

    # Default minutes to 00 if not provided
    m1 = int(m1) if m1 else 0
    m2 = int(m2) if m2 else 0
    h1 = int(h1)
    h2 = int(h2)

    # Validate hour and minute ranges
    if not (1 <= h1 <= 12 and 0 <= m1 < 60 and 1 <= h2 <= 12 and 0 <= m2 < 60):
        raise ValueError("Invalid time values")

    # Convert to 24-hour format
    h1_24 = h1 % 12 + (12 if p1 == "PM" else 0)
    h2_24 = h2 % 12 + (12 if p2 == "PM" else 0)

    return f"{h1_24:02}:{m1:02} to {h2_24:02}:{m2:02}"

if __name__ == "__main__":
    main()
