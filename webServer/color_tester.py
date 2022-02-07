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
            ledPix.twoColors(1, col1=(0, 0, 255), col2=(0,0,0))

        if T >= 21:
            ledPix.twoColors(2, col1=(0, 0, 100), col2=(0,0,0))

        if T >= 22:
            ledPix.twoColors(3, col1=(225, 40, 0))

        if T >= 23:
            ledPIx.twoColors(3, col1=(225, 40, 0))

        time.sleep(5)


ledPix.setColor((0, 0, 0,))
print("done")
