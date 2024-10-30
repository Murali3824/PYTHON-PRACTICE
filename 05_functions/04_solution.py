#  4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius. 

import math
r = int(input("enter the radius of the circle : "))

def cir(r):
    area = math.pi * r ** 2
    circumference  = 2 * math.pi * r
    return area,circumference

a,c = cir(r)
print("Area: ",round(a,2), "Circumference: ",round(c,2))
