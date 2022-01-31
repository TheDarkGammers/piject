from sensor_T import *
import asyncio
import time

sT = sensor_T(None)


for i in range(10):
    T = sT.read()
    print(i,T)
    time.sleep(5)
print("done")
