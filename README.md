# BadAppleAscii

Python Script that plays [Bad Apple](https://www.youtube.com/watch?v=FtutLA63Cp8) in the terminal.

## Setup

### Requirements

- [ffmpeg](https://ffmpeg.org/) is a program used to convert one file type to another.
- [pillow](https://pypi.org/project/Pillow/) is a program that allows for image processing.

### Installation

1. Clone this project:

```
git clone https://github.com/Susarog/BadAppleAscii.git
```

2. Download [Bad Apple](https://www.youtube.com/watch?v=FtutLA63Cp8) in an mp4 file format

3. Move the mp4 file in a directory called frames in the cloned repository

4. Use ffmpeg to convert the mp4 video to jpg images in intervals of 30 frames per second

```
ffmpeg -i bad-apple.mp4 -vf fps=30 ./out%04d.jpg
```

4. Run setup.py

```
python3 setup.py ./frames/images
```

5. Run main.py

```
python3 main.py ./frames/text
```
