"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module3_day40_image.py
    Creation Date:  7/6/2019, 4:11 PM
    Description:    Python Automation Program 12: Image Manipulations
"""

import os
from PIL import Image

os.chdir(".\\images")

# The `.open()` function is used to open the image as a pillow image object. Attributes of the image can be called using
# various variables, such as `.size`, `.filename`, `.format`, and `.format_description`.
oldest = Image.open("oldest.jpg")
width, height = oldest.size
print(f"Filename: {oldest.filename}\nFormat: {oldest.format}\nFormat Description: {oldest.format_description}\n"
      f"Size: {width}x{height}")

print("=" * 50)

# With a file open, the `.crop()` function can be utilized to crop the image. The function takes a tuple input with the
# format `(left, upper, right, lower)` for the numerical pixel coordinates. The numerical pixel locations can be used,
# but the function also allows the coordinates to be determined using formulas. The cropped image can then be saved with
# the `.save()` function. The output format does not need to match the input format.
middlest = Image.open("middlest.png")
cropped = middlest.crop((115, 5, 385, 275))
cropped.save("middlest_cropped.png")

segment = (width - height) / 2
cropped = oldest.crop((segment, 0, width - segment, 270))
cropped.save("oldest_cropped.png")

old_crop = Image.open("oldest_cropped.png")
width, height = old_crop.size
print(f"Filename: {old_crop.filename}\nFormat: {old_crop.format}\nFormat Description: {old_crop.format_description}\n"
      f"Size: {width}x{height}")

print("=" * 50)

# Apart from cropping an image, the `.resize()` function is used to first change the canvas size before conducting the
# `.crop()` function. This function only accepts integer tuples for the new width and height values. Using formulas to
# alter the size allows the image to retain the same aspect ratio.
sweetbaby = Image.open("sweetbaby.jpg")
width, height = sweetbaby.size
resized = sweetbaby.resize((int(width / 1.3), int(height / 1.3)))
cropped = resized.crop((222, 100, 762, 370))
cropped.save("sweetbaby_cropped.png")

# The `.new()` function creates a new canvas with a specific color mode (`RGBA`) and tuple size (`540x540`). Image
# objects can then be added to the canvas using the `.paste()` function. This takes the image object and a tuple
# location, `(left, top)`, as inputs. The resulting image object can then be saved as the final collage.
oldest = Image.open("oldest_cropped.png")
middlest = Image.open("middlest_cropped.png")
sweetbaby = Image.open("sweetbaby_cropped.png")

mbmbam = Image.new("RGBA", (540, 540))
mbmbam.paste(oldest, (0, 0))
mbmbam.paste(middlest, (271, 0))
mbmbam.paste(sweetbaby, (0, 271))
mbmbam.save("mbmbam.png")

# The Pillow package also contains a `.convert()` function which can be utilized to quickly change an image from color
# to greyscale.
greyscale = mbmbam.convert(mode="L")
greyscale.save("mbmbam_bw.png")
