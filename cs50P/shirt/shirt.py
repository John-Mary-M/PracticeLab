"""cs50p 18/10/2023 FILE I/O problemset 6 shirt.py"""

import sys
import os
from PIL import Image, ImageOps



def main():
    """Entry point"""
    check()
    overylay(sys.argv[1], sys.argv[2])


def check():
    """checks program reqirements"""

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguements")
    # if (
    #     not sys.argv[1].endswith("png")
    #     or not sys.argv[1].endswith("jpg") or not sys.argv[1].endswith("jpeg")
    # ):
    #     sys.exit("Input and output have different extensions")
    file_1 = os.path.splitext(sys.argv[1])
    print(file_1)
    file_2 = os.path.splitext(sys.argv[2])
    print(file_2)
    if extension_chk(file_1) is False:
        sys.exit("Ivalid input")
    if extension_chk(file_2) is False:
        sys.exit("Ivalid output")
    if file_1[1].lower() != file_2[1].lower():
        sys.exit("Iput and output have different extensions")
    # if (
    #     not sys.argv[2].endswith("png")
    #     or not sys.argv[2].endswith("jpg") or not sys.argv[2].endswith("jpeg")
    # ):
    #     sys.exit("Input and output have different extensions")
    # if not sys.argv[1]:
    #     sys.exit("Ivalid input")
    # return True

def extension_chk(file):
    """checks file extension"""
    if file[1] in [".jpg", ".jpeg", ".png"]:
        return True
    return False
def overylay(image_in, image_out):
    """Takes the two commandline arguments as
    image_in which is sys.argv[1] and overlays it on
    image_out which is sys.argv[2]
    Returns a new image that is a combination of the two
    command-line arguements
    """
    try:
        image_file = Image.open(image_in)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt_image = Image.open("shirt.png")
    # get shirt size
    size = shirt_image.size
    # resize the muppet
    muppet =ImageOps.fit(image_file, size)
    # paste
    muppet.paste(shirt_image, shirt_image)
    # save new image
    muppet.save(image_out)

if __name__ == "__main__":
    main()
