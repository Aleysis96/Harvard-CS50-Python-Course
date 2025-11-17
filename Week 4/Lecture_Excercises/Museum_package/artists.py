import requests

# Function to search for artists using the Art Institute of Chicago API
def artistas(query, limit):
    try:
        # Send a GET request with search query and result limit
        response = requests.get(
            "https://api.artic.edu/api/v1/agents/search", {"q": query, "limit": limit}
        )
        # Raise an error if the response status is not successful
        response.raise_for_status()
    except requests.HTTPError:
        # If an HTTP error occurs, return an empty list
        return []

    # Parse the JSON response
    content = response.json()

    # Extract and return the list of artist titles
    return [artist["title"] for artist in content["data"]]
