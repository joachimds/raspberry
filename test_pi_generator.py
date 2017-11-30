from math import sqrt
from random import random

counter1 = 0
counter2 = 1000000

for i in range (1,counter2):
    x = random()
    y = random()
    
    if x+y > 0:
        z = sqrt (x**2 + y**2)
        if (z <= 1):
            counter1 += 1
    else:
        counter1 += 1

pi = counter1/counter2 * 4

print (pi)
    
