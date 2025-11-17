def main():
    x = int(input("number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

# Full program flow:
# - main() is executed by the final line main().
# - Inside def main(), a number is requested from the user.
# - is_even(n) is called within the if statement.
# - Depending on the result (True or False), "Even" or "Odd" is printed.

