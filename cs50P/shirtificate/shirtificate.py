"""cs50p problemset 8 12/11/2023
    shirtificate.py, implement a program that prompts the user for
    their name and outputs, using fpdf2, a CS50 shirtificate in a
    file called shirtificate.pdf
"""
from fpdf import FPDF
# from PIL import Image

def main():
    """Entry Point"""
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", size=30)
    # pdf.cell(0, 60, 'CS50 Shirtificate', 0, 1, 'C')

    # title
    pdf.set_xy(0, 30)
    pdf.cell(0, 0, 'CS50 Shirtificate', 0, 1, 'C')

    # geting image dimensions
    image_path = "/home/johnmary/C_code/PracticeLab/cs50P/shirtificate/shirtificate.png"
    # with Image.open(image_path) as img:
    #     img_width, img_height = img.size

    # Add the image
    pdf.set_xy(0, 160)
    pdf.image(image_path, x=0, y=40, w=200)

    # font color on the shirt
    pdf.set_text_color(255, 255, 255)
    # add text to the shirt
    pdf.cell(0, -85, f"{name} took CS50", 0, 1, 'C')

    # output
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
