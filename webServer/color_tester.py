from sensor_T import *
import asyncio
import time
import neopixel
from ledPixels import *

def F(T):
     return T*9/5+32





sT = sensor_T(None)

ledPix = ledPixels(20, board.D18)

with open('data.csv','w') as f:

    for i in range(0,25,5):
        T = sT.read()
        print(i,T,F(T))
        f.write(f"{i},{T}\n")


        if T >= 20:
            ledPix.twoColors(2, col1=(0, 0, 255), col2=(0, 0, 0))

        if T >= 21:
            ledPix.twoColors(4, col1=(225, 40, 20), col2=(0, 0, 0))

        if T >= 22:
            ledPix.twoColors(6, col1=(225, 40, 0), col2=(0, 0, 0))

        if T >= 23:
            ledPix.twoColors(8, col1=(225, 40, 0), col2=(0, 0, 0))

        if T >= 24:
            ledPix.twoColors(10, col1=(225, 40, 0), col2=(0, 0, 0))

        if T >= 25:
            ledPix.twoColors(12, col1=(225, 10, 0), col2=(0, 0, 0))

        if T >= 26:
            ledPix.twoColors(14, col1=(225, 0, 0), col2=(0, 0, 0))

        if T >= 27:
            ledPix.twoColors(16, col1=(225, 0, 0), col2=(0, 0, 0))

        if T >= 28:
            ledPix.twoColors(18, col1=(225, 0, 0), col2=(0, 0, 0))

        if T >= 29:
            ledPix.twoColors(19, col1=(225, 0, 0), col2=(0, 0, 0))

        if T >= 30:
            ledPix.twoColors(20, col1=(225, 0, 0), col2=(0, 0, 0))

        time.sleep(5)


ledPix.setColor((0, 0, 0,))
print("done")
