import math
import random
class circle:
    def circum(self):
        return 2*math.pi*self.radius
circles = []
for i in range(0,10):
    c = circle()
    c.radius = random.uniform(1.1,9.5)
    # c.circum = c.circum(c.radius) obj can't be called
    circles.append(c)
for c in circles:
    print("radius",c.radius,"circum",c.circum())
