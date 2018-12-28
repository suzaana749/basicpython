from __future__ import print_function
class Shape:     #parent
    def __init__(self):
        self.color ="red"
        self.sides = 0

class Square(Shape):  # child
    def __init__(self, w,c):
        Shape.__init__(self)  # method overridding
        self.width = w
        self.color = c

class Circle(Shape):    #child
    def __init__(self,r,c):
        Shape.__init__(self) #method overridding
        self.radius = r
        self.color = c
sq1 = Square(5,"green")
sq2 = Square(9,"black")
c1 = Circle(10,"orange")
print("square size", sq1.width, "x", sq1.sides, sq1.color, ",", sq2.width, "x", sq2.sides, sq2.color)
print("circle",c1.color,c1.radius)