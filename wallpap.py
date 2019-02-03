import ctypes, os, datetime
from PIL import Image, ImageDraw, ImageFont
import time as tt

counter = 0
prefix = "\\a\\frame_" #Change prefix of each filename
suffix = "_delay-0.04s_edit.gif" #Change suffix of each file name
numberOfFrames = 16 #Change number of frames for Gif
delayOfFrames = 0.04 #Change delay between frames

while 1:
    tt.sleep(delayOfFrames)
    if counter == numberOfFrames:
        counter = 0

    if counter < 10: #Only needed if below ten are still double digits with 0 in front
        filenameEdit = os.path.dirname(os.path.realpath(__file__)) + prefix + "0" + str(counter) + suffix
        filename = os.path.dirname(os.path.realpath(__file__)) + prefix + "0" + str(counter) + suffix
    else:
        filenameEdit = os.path.dirname(os.path.realpath(__file__)) + prefix + str(counter) + suffix
        filename = os.path.dirname(os.path.realpath(__file__)) + prefix + str(counter) + suffix

    counter += 1
#START adds a clock
    img = Image.open(filename)
    fnt = ImageFont.truetype('arial.ttf', 100)
    d = ImageDraw.Draw(img)

    time = datetime.datetime.now()
    text = time.strftime("%H") + " : " + time.strftime("%M") + " : " + time.strftime("%S")

    d.text((1350 , 900), text, font=fnt, fill=255)

    img.save(filenameEdit)
#END adds a clock
    pathToBmp = os.path.normpath(filenameEdit)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, pathToBmp , 0)
    print(filename)
