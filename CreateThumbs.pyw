#!/usr/bin/env python3
Version = "Create Thumbs 1.0"

import io
import os
import sys
import PIL
from PIL import Image

baseheight = 600
img = Image.open("/home/pi/Pictures/" + sys.argv[1])
img = img.resize((int((float(img.size[0]) * float(baseheight / float(img.size[1])))), baseheight), PIL.Image.ANTIALIAS)
img.save("/home/pi/Pictures/Thumbs/" + sys.argv[1])


for file in os.listdir("/home/pi/Pictures/Thumbs/"):
    try:
        imageTest = open("/home/pi/Pictures/" + file)
    except IOError:
        os.remove("/home/pi/Pictures/Thumbs/" + file)
    finally:
        imageTest.close()



