def main():
    x = get_num() # takes the value from function below
    print(f"x is {x}")

def get_num():
    while True:
        try:
            x = int(input("Enter number: "))
            return x
        except ValueError:
            pass # except of printing an error message, just ask again the main question

main()

# You can code return x after the input, just like the break
