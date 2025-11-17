# implement a program to obtain bitcoin price
import requests
import sys

if len(sys.argv) > 1: # Check if a command-line argument was provided
    try:
        argument = float(sys.argv[1]) # Convert the argument to a float (e.g., number of Bitcoins)
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=8b141b528da8a2fec5f7657bbb2fa90dc9e5d561864b13a331334a5765c39546")
        # Send a GET request to the CoinCap API to fetch Bitcoin data

        o = response.json() # Parses the JSON response into a Python dictionary

        price_usd_str = o["data"]["priceUsd"] # Extract the price of Bitcoin in USD (as a string)
        price_usd = float(price_usd_str) # Convert the price to a float
        result = argument * price_usd # Multiply the user-provided amount by the current price

        print(f"${result:,.4f}") # Print the result formatted as currency with 4 decimal places
    except requests.RequestException: # Handle network or API errors
        print("Couldn't complete request")
        sys.exit(1)
    except ValueError: # Handle invalid numeric input
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument") # Handle missing command-line argument
    sys.exit(1)


# if len(sys.argv) > 1: it means that 1 and more arguments was passed in command line (e.g. bitcoin.py 1)
# sys.argv by default is the name of the py file only (bitcoin.py), so by adding > 1 it tells that another argument after the py file was entered

