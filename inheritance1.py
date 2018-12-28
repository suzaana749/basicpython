from __future__ import print_function
class Shape:     #parent
    def __init__(self):
        self.color ="red"
        self.sides = 0
class Square(Shape):    #child
    def __init__(self,w):
        Shape.__init__(self) #method overridding
        self.width = w
sq1 = Square(5)
sq2 = Square(9)
print("square size",sq1.width,"x",sq1.sides,sq1.color,",",sq2.width,"x",sq2.sides,sq2.color)