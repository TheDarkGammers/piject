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
        elif T >= 25:
            ledPix.setColor((255, 0, 0,))
        else:
            ledPix.setColor((255, 40, 0,))
            self.brightness(1, 0):
        time.sleep(5)


ledPix.setColor((0, 0, 0,))
print("done")
