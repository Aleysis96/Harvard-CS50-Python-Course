def main():
    test()

def test():
    n = input("first number? ")
    n2 = input("second number? ")
    if n.isdigit() and n2.isdigit():
        n = int(n)
        n2 = int(n2)
        result = n * n2
        print(result)
    else:
        print("invalid")


main()
