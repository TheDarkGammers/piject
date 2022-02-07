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


        if T <= 20:
            ledPix.setColor((0, 0, 255))
            ledPix.twoColors(6, col1=(0,0,255), col2=(0,0,0))
        elif T >= 25:
            ledPix.setColor((255, 0, 0,))
            ledPix.twoColors(20, col1=(255, 0, 0), col2=(0,0,0))
        else:
            ledPix.setColor((255, 40, 0,))
            ledPix.twoColors(12, col1=(255, 40, 0), col2=(0,0,0))
        time.sleep(5)


ledPix.setColor((0, 0, 0,))
print("done")
