import os
import sys
import time
import re


def main():
    txt_dir = sys.argv[1]
    files_txt = os.listdir(txt_dir)
    sorted_filenames = sorted(files_txt, key=lambda x: float(re.findall("(\d+)", x)[0]))
    for i in range(0, len(sorted_filenames)):
        filePath = os.path.join(txt_dir, sorted_filenames[i])
        with open(filePath, "r") as f:
            print(f.read())

        time.sleep(1 / 30)


main()
