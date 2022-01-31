from sensor_T import *
import asyncio
import time

sT = sensor_T(None)

with open('data.csv','w') as f:

    for i in range(0,25,5):
        T = sT.read()
        print(i,T)
        f.write(f"{i},{T}")
        time.sleep(5)
print("done")
