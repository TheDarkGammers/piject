import asyncio
import time
import neopixel
from ledPixels import *




ledPix = ledPixels(20, board.D18)

print("start")

for i in range(0,5,1):
    ledPix.setColor((255, 120, 0,))
    time.sleep(1)


ledPix.setColor((0, 0, 0,))
print("done")
