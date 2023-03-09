import PIL.Image
import os
import sys

DENSITY_CHAR = [" ", ".", ",", ":", ";", "°", "*", "o", "O", "#", "@"]


def to_greyscale(image):
    return image.convert("L")


def pixel_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    desnity_length = len(DENSITY_CHAR)
    for pixel in pixels:
        ascii_str += DENSITY_CHAR[round((desnity_length - 1) * pixel) // 255]
    return ascii_str


def resize(image, new_width=50, new_height=25):
    return image.resize((new_width, new_height))


def main():
    image_file = sys.argv[1]
    image = PIL.Image.open(image_file)
    image = resize(image)
    image = to_greyscale(image)
    ascii_str = pixel_to_ascii(image)
    ascii_str_len = len(ascii_str)
    img_width = image.width
    ascii_img = ""
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i : i + img_width] + "\n"
    print(ascii_img)


main()
