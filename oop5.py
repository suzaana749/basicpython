from __future__ import print_function
import math
import random
class circle:
    def calCircum(self):
        return 2*math.pi*self.radius
    def calDiameter(self):
        return self.radius *2
    def calArea(self):
        return math.pi * (self.radius ** 2)
    def __init__(self):   # constructor function called
        self.radius - random.uniform(1.1,10.5)
circles = []
for i in range(0,10):
    c = circle()
    #c.radius = random.uniform(1.1,10.5)
    circles.append(c)
for c in circles:
    print("radius",round(c.radius,2),"circum",round(c.calCircum(),2),"diameter",round(c.calDiameter(),2),"area",round(c.calArea(),2))

