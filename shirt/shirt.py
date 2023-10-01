import sys
import os
from PIL import Image
from PIL import ImageOps

def main():
    try:
        check_input()

        before = sys.argv[1]
        after = sys.argv[2]

        shirt = Image.open("shirt.png")
        new_width,new_height = shirt.size

        image = Image.open(before)

        width,height = image.size()

        left = (width - new_width)/2
        top = (height - new_height)/2
        right = (width + new_width)/2
        bottom = (height + new_height)/2

        image = image.crop((left, top, right, bottom))

        new_image.save(after)



    except FileNotFoundError:
        sys.exit("Input does not exist")

def check_input():
    if len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")

    _,extention1 = sys.argv[1].split(".")
    _,extention2 = sys.argv[2].split(".")

    if extention1 != extention2:
        sys.exit("Input and output have different extensions")
    if extention2 == "png" or extention2 == "jpg" or extention2 == "jpeg":
        pass
    else:
        sys.exit("Invalid output")

main()