from PIL import Image
from PIL import ImageFilter

def main():
    with Image.open("in.jpeg") as img:
        img = img.rotate(180)
        img.filter(ImageFilter.BLUR)
        img.save("out.jpg")

main()

# have to create another file (image_downloaded.py) requesting the image and downloading it from internet
# due to unabled to import the image as a file from my computer.
# the file downloaded was a normal image as it is original, so the out file looks rotated, different from the excersice.
