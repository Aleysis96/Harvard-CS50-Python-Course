import csv
import sys

# Validate number of command-line arguments

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) >= 4:
    sys.exit("Too many command-line arguments")


input_file = sys.argv[1]
output_file = sys.argv[2]

# Try to open the input CSV
try:
    with open(input_file, "r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        students = []

        for row in reader:
            full_name = row["name"]
            house = row["house"]

            # Split full name into first and last
            if "," in full_name:
                last, first = full_name.split(", ")
            else:
                sys.exit(f"Invalid name format: {full_name}")

            students.append({"first": first, "last": last, "house": house})

except FileNotFoundError:
    sys.exit(f"Could not read {input_file}")

# Write to the output CSV
with open(output_file, "w", newline="") as outfile:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)



