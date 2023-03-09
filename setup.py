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


def setup():
    frames_images = sys.argv[1]
    text_dir = frames_images + "/../text/"
    os.makedirs(text_dir, exist_ok=True)
    file_images = os.listdir(frames_images)
    sorted_filenames = sorted(file_images)
    for i in range(0, len(sorted_filenames)):
        f = os.path.join(frames_images, sorted_filenames[i])
        if os.path.isfile(f):
            image = PIL.Image.open(f)
            image = resize(image)
            image = to_greyscale(image)
            ascii_str = pixel_to_ascii(image)
            ascii_str_len = len(ascii_str)
            img_width = image.width
            ascii_img = ""
            out_file = text_dir + "ascii_image" + str(i) + ".txt"
            for i in range(0, ascii_str_len, img_width):
                ascii_img += ascii_str[i : i + img_width] + "\n"
                with open(out_file, "w") as f:
                    f.write(ascii_img)


setup()
