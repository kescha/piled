#!/usr/bin/env python
import time
import os
from samplebase import SampleBase
from PIL import Image


class Emoji(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Emoji, self).__init__(*args, **kwargs)
        #self.parser.add_argument("-i", "--image", help="The image to display", default="../../../examples-api-use/runtext.ppm")

    def run(self):
        images = []
        for (dirpath, dirnames, filenames) in os.walk("../cutouts"):
            for filename in filenames:
                if filename.endswith('.png'):
                    image = os.sep.join([dirpath, filename])
                    image.resize((self.matrix.width, self.matrix.height), Image.ANTIALIAS)
                    images.append(image)

        double_buffer = self.matrix.CreateFrameCanvas()

        # let's scroll
        images_amount = len(images)
        pos = 0
        while True:
            pos += 1
            if pos > images_amount:
                pos = 0

            image = image[pos]

            double_buffer.SetImage(image)

            double_buffer = self.matrix.SwapOnVSync(double_buffer)
            time.sleep(0.01)


# Main function
# e.g. call with
#  sudo ./emoji.py --chain=4
# if you have a chain of four
if __name__ == "__main__":
    emojii = Emoji()
    if not emojii.process():
        emojii.print_help()
