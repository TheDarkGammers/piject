from sensor_T import *
import asyncio
import time

def F(T):
     return T*9/5+32





sT = sensor_T(None)


with open('data.csv','w') as f:

    for i in range(0,25,5):
        T = sT.read()
        print(i,T,F(T))
        f.write(f"{i},{T}\n")
        time.sleep(5)



print("done")
