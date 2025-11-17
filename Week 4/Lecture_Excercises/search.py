from Museum_package.artwork import get_artworks
from Museum_package.artists import artistas

# Main function to prompt user input and display matching artists
def main():
    # Ask the user to enter an artwork name or keyword
    artista = input("Artwork: ")

    # Search for up to 3 matching artists using the query
    creator = artistas(query=artista, limit=3)

    # Print each artist name in a bulleted list
    for artista in creator:
        print(f"* {artista}")

# Run the main function
main()
