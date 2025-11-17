# Main function to extract a portion of text from a file and save it as a new file
def main():
    # Open the original text file and read all lines into a list
    with open("alice.txt", "r") as f:
        contents = f.readlines()

    # Extract lines corresponding to Chapter 1 (lines 52 to 271)
    chapter1 = contents[52:272]

    # Write the extracted lines to a new file
    with open("chapter1.txt", "w") as f:
        f.writelines(chapter1)

# Run the main function
main()
