import sys
import os
from PIL import Image, ImageOps

# Validate number of arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

input_path = sys.argv[1]
output_path = sys.argv[2]

# Validate file extensions
valid_extensions = (".jpg", ".jpeg", ".png")
input_ext = os.path.splitext(input_path)[1].lower()
output_ext = os.path.splitext(output_path)[1].lower()

if input_ext not in valid_extensions or output_ext not in valid_extensions:
    sys.exit("Invalid output")

if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

# Validate input file existence
if not os.path.isfile(input_path):
    sys.exit("Input does not exist")

# Process image
try:
    shirt = Image.open("shirt.png")
    input_image = Image.open(input_path)

    # Resize and crop input to match shirt size
    resized = ImageOps.fit(input_image, shirt.size)

    # Overlay shirt.png
    resized.paste(shirt, shirt)

    # Save output
    resized.save(output_path)

except Exception as e:
    sys.exit(f"Error processing image: {e}")
