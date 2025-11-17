import requests

# Function to search for artworks using the Art Institute of Chicago API
def get_artworks(query, limit):
    try:
        # Send a GET request with the search query and result limit
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": query, "limit": limit}
        )
        # Raise an error if the response status is not successful
        response.raise_for_status()
    except requests.HTTPError:
        # If an HTTP error occurs, return an empty list
        return []

    # Parse the JSON response
    content = response.json()

    # Extract and return the list of artwork titles
    return [artwork["title"] for artwork in content["data"]]
