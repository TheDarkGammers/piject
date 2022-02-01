from sensor_T import *
import asyncio
import time
import neopixel
from ledPixels import *


sT = sensor_T(None)

ledPix = ledPixels(20, board.D18)

with open('data.csv','w') as f:

    for i in range(0,25,1):
        T = sT.read()
        print(i,T)
        f.write(f"{i},{T}\n")
        time.sleep(5)

        if T <= 25:
            ledPix setColor((0, 0, 255))

print("done")
