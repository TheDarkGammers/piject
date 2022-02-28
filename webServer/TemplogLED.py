from sensor_T import *
import asyncio
import time
import neopixel
from ledPixels import *
from datetime import datetime
import argparse



def F(T):
     return T*9/5+32
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--dt", default=5, type=float, help = "Time Step")



dt = args.dt

sT = sensor_T(None)

ledPix = ledPixels(20, board.D18)


with open('data.csv','w') as f:
    d = datetime.now()
    f.write(d.isoformat()+ " " + d.ctime())
    i = 0
    while True:
        T = sT.read()
        print(i,T,F(T))
        f.write(f"{i*dt}, {T}, {F(T)}\n")


        if T <= 19:
            ledPix.twoColors(6, col1=(0,0,255), col2=(0,0,0))
        elif T >= 26:
            ledPix.twoColors(20, col1=(255, 0, 0), col2=(0,0,0))
        else:
            ledPix.twoColors(12, col1=(255, 40, 0), col2=(0,0,0))
        time.sleep(dt)
        i = i + 1

ledPix.setColor((0, 0, 0,))
print("done")
