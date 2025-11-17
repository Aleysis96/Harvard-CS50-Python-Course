import sys
from PIL import Image

# Create an empty list to store the opened images
images = []

# Loop through all command-line arguments except the script name
for arg in sys.argv[1:]:
    # Open each image file and add it to the list
    image = Image.open(arg)
    images.append(image)

# Save the first image as a GIF, appending the second image to create an animation
images[0].save(
    "costumes.gif",           # Output filename
    save_all=True,            # Save all frames, not just the first
    append_images=[images[1]],# Add the second image as the next frame
    duration=200,             # Duration between frames in milliseconds
    loop=0                    # Loop forever (0 = infinite loop)
)
