"""cs50p 18/10/2023 FILE I/O problemset 6 shirt.py"""

import sys
from PIL import Image, ImageOps


def main():
    """Entry point"""
    check()


def check():
    """checks program reqirements"""

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguements")
    if (
        not str(sys.argv[1], sys.argv[2]).endswith("png")
        or str(sys.argv[1], sys.argv[2]).endswith("jpg")
        or str(sys.argv[1], sys.argv[2]).endswith("jpeg")
    ):
        sys.exit("Input and output have different extensions")
    if not sys.argv[1]:
        sys.exit("Ivalid input")
    return True


def overylay(image_in, image_out):
    """Takes the two commandline arguments as
    image_in which is sys.argv[1] and overlays it on
    image_out which is sys.argv[2]
    Returns a new image that is a combination of the two
    command-line arguements
    """
    # try:
    size = (211, 211)
    # open the base image
    base_image = Image.open(image_in)
    # Open the overlay
    overlay = Image.open("shirt.png")
    # Resize overlay image to the default size
    overlay = ImageOps.fit(overlay, size, method=0, bleed=0.0, centering=0)
    # Composite the overlay image on top of the base image
    base_image.paste(overlay, (0, 0), overlay)
    # Save the result as the output image
    base_image.save(image_out)
    return image_out
    # except Exception:
    #     pass


if __name__ == "__main__":
    main()
