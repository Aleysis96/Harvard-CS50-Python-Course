import csv
import sys
from tabulate import tabulate

# Initialize an empty list to store table rows
table = []

# Check the number of command-line arguments
if len(sys.argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) >= 3:
    print("Too many command-line arguments")
    sys.exit(2)

# Get the filename from the command-line argument
file = sys.argv[1]

# Ensure the file has a .csv extension
if not file.endswith(".csv"):
    print("Not a CSV file")
    sys.exit(3)

# Try to open and read the specified CSV file
try:
    if file == "regular.csv":
        with open("regular.csv", "r") as f:
            reader = csv.reader(f)
            header = next(reader)  # Read the header row
            for fila in reader:
                table.append(fila)  # Append each row to the table

    elif file == "sicilian.csv":
        with open("sicilian.csv", "r") as f:
            reader = csv.reader(f)
            header = next(reader)
            for fila in reader:
                table.append(fila)

except FileNotFoundError:
    print("File does not exist")
    sys.exit(4)

# Print the table using the tabulate module with a grid format
print(tabulate(table, headers=header, tablefmt="grid"))
