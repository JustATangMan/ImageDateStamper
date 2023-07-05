from PIL import Image, ExifTags, ImageDraw, ImageFont, ImageOps
from PIL.ExifTags import TAGS
import glob
import os
import time
import gc

# 256, width
# 257, length
# 274, orientation
# 306, date

os.chdir("./Photos")
os.mkdir("./Dated")


def print_stats(image):
    exif = image.getexif()
    width = exif.get(256)
    length = exif.get(257)
    date = exif.get(306)
    if date is not None:
        date = date.split()[0]
    orient = exif.get(274)
    # print("width: " + str(width) + " length: " + str(length) + " date: " + str(date) + " orient: " + str(orient))
    return width, length, orient, date


for file in glob.glob("*.jpg"):
    filename, extension = os.path.splitext(file)
    im = Image.open(filename + extension)
    im = ImageOps.exif_transpose(im)
    im_width, im_length, im_orient, im_date = print_stats(im)
    if im_width is None:  # no exif data use file data
        im_width = im.width
        im_length = im.height
        im_date = time.ctime(os.path.getctime(filename + extension)).split()  # parse file date, exclude day of week and time
        im_date.pop(3)
        im_date.pop(0)
        im_date = " ".join([str(x) for x in im_date])
    elif im_orient is None:  # exif oriented, swap length and width
        hold = im_width
        im_width = im_length
        im_length = hold
    draw = ImageDraw.Draw(im)
    os.chdir("../")
    size = ((im_width + im_length) // 50)
    if size < 10:
        size = 10
    if size > 100:
        size = 100
    font = ImageFont.truetype("Arial.ttf", size)
    os.chdir("./Photos")
    draw.text((im_width * 0.8, im_length * 0.95), str(im_date), (255,0,0), font)
    im = im.convert('RGB')
    os.chdir("./Dated")
    im.save(filename + extension, "JPEG")
    os.chdir("../")
    # del font
    # gc.collect()
