from PIL import Image, ExifTags, ImageDraw, ImageFont, ImageOps
from PIL.ExifTags import TAGS
import glob, os

# 256, width
# 257, length
# 274, orientation
# 306, date

font = ImageFont.truetype("Arial.ttf", 50)
os.chdir("./Photos")


def print_stats(image):
    exif = image.getexif()
    width = exif.get(256)
    length = exif.get(257)
    date = exif.get(306)
    orient = exif.get(274)
    print("width: " + str(width) + " length: " + str(length) + " date: " + str(date) + " orient: " + str(orient))
    return width, length, orient, date


for file in glob.glob("*.jpg"):
    filename, extension = os.path.splitext(file)
    print(filename)
    im = Image.open(filename + extension)
    im = ImageOps.exif_transpose(im)
    im_width, im_length, im_orient, im_date = print_stats(im)
    draw = ImageDraw.Draw(im)
    if im_orient is None:
        draw.text((im_length*0.80, im_width*0.95), str(im_date), None, font)
    else:
        draw.text((im_width * 0.85, im_length * 0.95), str(im_date), None, font)
    im.save("dated_" + filename + extension, "JPEG")
