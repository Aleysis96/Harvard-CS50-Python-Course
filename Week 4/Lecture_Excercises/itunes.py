import json # Imports the JSON module to handle JSON data
import requests # Imports the requests module to make HTTP requests
import sys # Imports the sys module to access command-line arguments

if len(sys.argv) != 2: # Checks if exactly one argument (besides the script name) was provided
    sys.exit()

# Sends a GET request to the iTunes Search API with the provided search term
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])

o = response.json() # Parses the JSON response into a Python dictionary

# Loops through the list of results and prints the name of each track
for result in o["results"]: # in the json text/file there is a key call "results"
    print(result["trackName"]) # we are calling the value from the key "trackName"


# a JSON is basically a dictionary with keys and values
