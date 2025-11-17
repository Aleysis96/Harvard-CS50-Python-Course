def main():
    hello("world") # Calls the hello function with the argument "world"
    goodbye("world") # Calls the goodbye function with the argument "world"


def hello(name):
    print(f"hello, {name}") # Prints "hello" followed by the given name

def goodbye(name):
    print(f"goodbye, {name}") # Prints "goodbye" followed by the given name


if __name__=="__main__": # Ensures that the main function runs only when the script is executed directly,
    main()
