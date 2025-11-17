import sys

def count_code_lines(file_path):
    try:
        with open(file_path, "r") as f: # Open the file in read mode
            inside_docstring = False # Flag to track if we're inside a docstring
            code_lines = 0 # Counter for code lines

            for line in f:
                line = line.strip() # Remove leading/trailing whitespace

                # Skip blank lines
                if not line:
                    continue

                # Skip single-line comments
                if line.startswith("#"):
                    continue

                # Detect start or end of docstring
                if line.startswith('"""') or line.startswith("'''"):
                    if not inside_docstring:
                        inside_docstring = True
                        continue
                    else:
                        inside_docstring = False
                        continue

                # Skip lines inside docstrings
                if inside_docstring:
                    continue

                # Count as code
                code_lines += 1

            return code_lines

    except FileNotFoundError: # Handle case where file does not exist
        print("File does not exist")
        return None

if len(sys.argv) == 1: # if only current py file name is entered
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) >= 3: # if more than 3 py files names are entered
    print("Too many command-line arguments")
    sys.exit(1)

file = sys.argv[1]

if not file.endswith(".py"): # Validate that the file has a .py extension
    print("Not a Python file")
    sys.exit(3)

total = count_code_lines(file) # Count and print the number of code lines
if total is not None:
    print(total)

# to read file lines of codes, file to read needs to be within the same lines.py folder
