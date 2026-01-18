#Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
# the area of a circle is A=pi * r^2

import math
radius= float (input("Enter radius: "))
#print(radius)
radius_square= radius**2
#print(radius_square)
area= math.pi * radius_square
print(f"So, the area of a circle is:{area:.3f}")



