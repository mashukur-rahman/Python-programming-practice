#Write the Python code of a program that reads the radius of a circle and prints its circumference and area.
import math
radius=int(input('Enter the radius of the circle: '))
circumference=2*math.pi*radius
area=math.pi*(radius**2)
print(circumference)
print(area)