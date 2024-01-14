#a python program that calculates the area of a circle given the radius

def area(radius):
    PI = 3.142
    return (PI*radius*radius)

radius = float(input("Enter radius: "))
print("The area is: {} ".format(area(radius)))
