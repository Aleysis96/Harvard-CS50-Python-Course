# Define a function that accepts any number of positional and keyword arguments
def f(*args, **kwargs):
    # Print the dictionary of keyword arguments
    print("Named:", kwargs)

# Call the function with named arguments representing magical currency
f(galleons=100, sickles=50, knuts=25)
