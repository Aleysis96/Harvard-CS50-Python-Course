import requests # Imports the requests library to make HTTP requests

def main(): # Defines the main function that runs the search logic
    print("Search the Art: ")
    artist = input("Artis: ") # Asks the user to enter an artist's name

    try:
        response = requests.get( # Sends a GET request to the Art Institute of Chicago API with the artist's name as a query
            "https://api.artic.edu/api/v1/artworks/search", {"q": "artist"}
            )
        response.raise_for_status() # Raises an error if the response status is not OK (e.g., 404 or 500)
    except requests.HTTPError:
        print("Couldn't complete request") # Prints an error message if the request fails
        return # Exits the function
    content = response.json() # Parses the JSON response into a Python dictionary

    if not content.get("data"): # if user inputs a non existen name within the database, shows the message
        print(f"Cannot search {artist}, please enter correct name")

    for artwork in content["data"]: # Loops through the list of artworks and prints each title
        print(f"* {artwork['title']}")

main()
