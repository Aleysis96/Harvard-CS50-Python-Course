#  implement a function called parse that expects a str of HTML as input,
# extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and returns its shorter, shareable youtu.be

import re

# Main function to prompt user input and extract a YouTube short link
def main():
    # Ask the user to enter an HTML snippet and print the parsed result
    print(parse(input("HTML: ")))

# Function to extract a YouTube video ID from an iframe and return a shortened URL
def parse(s):
    # Regular expression pattern to match a YouTube embed iframe and capture the video ID
    pattern = r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"[^>]*></iframe>'

    # Search for the pattern in the input string
    if match := re.search(pattern, s):
        video_id = match.group(1)  # Extract the video ID from the match
        return f"https://youtu.be/{video_id}"  # Return the shortened YouTube URL
    else:
        return "None"  # Return "None" if no match is found

# Run the main function only if this script is executed directly
if __name__ == "__main__":
    main()
