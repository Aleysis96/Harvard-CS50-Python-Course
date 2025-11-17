import csv
import numpy as np
from PIL import Image

# Main function to read view data, calculate brightness, and write analysis
def main():
    # Open the input CSV file and the output CSV file
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        # Read the input CSV as a dictionary
        reader = csv.DictReader(views)

        # Prepare the writer with an extra "brightness" column
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        # Process each row in the input CSV
        for row in reader:
            # Calculate brightness from the corresponding image file
            row["brightness"] = round(calculate_brightness(f"{row['id']}.jpeg"), 2)

            # Write the updated row to the output CSV
            writer.writerow(row)

# Function to calculate brightness of an image file
def calculate_brightness(filename):
    # Open the image and convert it to grayscale
    with Image.open(filename) as image:
        # Compute the average pixel intensity and normalize to [0, 1]
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness

# Run the main function
main()

