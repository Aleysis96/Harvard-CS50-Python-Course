# Define a recursive function to calculate the factorial of a number
def factorial(n):
    # Base case: factorial of 1 is 1
    if n == 1:
        return 1
    # Recursive case: multiply n by the factorial of (n - 1)
    return n * factorial(n-1)

# Call the factorial function with input 3 and store the result
result = factorial(3)
