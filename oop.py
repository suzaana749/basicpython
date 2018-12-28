import math
def circum(a):
    return 2*math.pi*a
# a= float(input("enter r"))
# print("value is",a)

# circleName = "first circle"
# circleRadius = 4.4
# circle2Name = "second circle"
# circleRadius = 3.2
# circle3Name = "third circle"
# circleRadius = 5.4
# circum1 = circum(circleRadius)
# circum2 = circum(circleRadius)
# circum3 = circum(circleRadius)
# print(circum1,circleName)
# print(circum2,circle2Name)
# print(circum3,circle3Name)

circles = [["first circle",4,4,0],["second circle",3,7,0],["third circle",8,4,0]]
circles[0][2] = circum(circles[0][1])
print(circles[0][2])
