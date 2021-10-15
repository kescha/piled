#!/usr/bin/env python3
import time
import os
from samplebase import SampleBase
from rgbmatrix import graphics
from PIL import Image
from weather import fetch_weather


class Emoji(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Emoji, self).__init__(*args, **kwargs)
        #self.parser.add_argument("-i", "--image", help="The image to display", default="../../../examples-api-use/runtext.ppm")

    def run(self):
        images = []
        for (dirpath, dirnames, filenames) in os.walk("../../cutouts"):
            for filename in filenames:
                if filename.endswith('.png'):
                    image_file = os.sep.join([dirpath, filename])
                    image = Image.open(image_file).convert('RGB')
                    image = image.resize((48, 48), Image.ANTIALIAS)
                    images.append(image)

        double_buffer = self.matrix.CreateFrameCanvas()


        # fonts
        font = graphics.Font()
        font.LoadFont("../../fonts/6x13.bdf")
        text_color = graphics.Color(255, 255, 0)
        my_text = "{0}°C"

        # let's scroll
        images_amount = len(images)
        pos = 0
        while True:
            pos += 1
            if pos >= images_amount:
                pos = 0

            image = images[pos]

            double_buffer.SetImage(image, 0, 12)

            weather_data = fetch_weather("45128")
            graphics.DrawText(double_buffer, font, 37, 10, text_color, my_text.format(weather_data['main']['temp']))

            double_buffer = self.matrix.SwapOnVSync(double_buffer)
            time.sleep(20)


# Main function
# e.g. call with
#  sudo ./emoji.py --chain=4
# if you have a chain of four
if __name__ == "__main__":
    emojii = Emoji()
    if not emojii.process():
        emojii.print_help()
