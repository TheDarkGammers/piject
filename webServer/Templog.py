from sensor_T import *
import asyncio
import time

sT = sensor_T(None)


for i in range(0,20,5):
    T = sT.read()
    print(i,T)
    time.sleep(5)
print("done")
