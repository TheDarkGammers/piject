import time
import neopixel
from ledPixels import *


ledPixels = ledPix

ledPix = ledPixels(20, board.D18)

for i in range(0,10,5):
    ledPix.setColor((255, 153, 51,))


ledPix.setColor((0, 0, 0,))
print("done")
