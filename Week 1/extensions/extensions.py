# implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends

def main():
    extension = input("File name: ").strip().lower() # we remove spaces and capitalized letters
    if extension.endswith("gif"):
        print("image/gif")
    elif extension.endswith("jpg"):
        print("image/jpeg")
    elif extension.endswith("jpeg"):
        print("image/jpeg")
    elif extension.endswith("png"):
        print("image/png")
    elif extension.endswith("pdf"):
        print("application/pdf")
    elif extension.endswith("txt"):
        print("text/plain")
    elif extension.endswith("zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main() # Calls the function
