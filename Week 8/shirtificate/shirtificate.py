

from fpdf import FPDF
from PIL import Image
import os

class Shirtificate(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 24)
        self.cell(0, 20, "CS50 Shirtificate", ln=True, align="C")

def main():
    name = input("Name: ")

    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Load image dimensions
    image_path = "shirtificate.png"
    if not os.path.exists(image_path):
        raise FileNotFoundError("shirtificate.png not found.")

    img = Image.open(image_path)
    img_width, img_height = img.size
    aspect_ratio = img_height / img_width

    # Resize image to fit page width
    page_width = 210
    margin = 20
    img_display_width = page_width - 2 * margin
    img_display_height = img_display_width * aspect_ratio
    x_pos = margin
    y_pos = 60

    pdf.image(image_path, x=x_pos, y=y_pos, w=img_display_width)

    # Overlay name in white text
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_y(y_pos + 60)  # Adjust based on shirt image position
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
