# 3. Write a program that asks the user for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides.

import math
#we know the perimeter is, P= 2(length + width) and the area is A= length * width

recLength= float(input("Enter the length of the rectangle: "))
recWidth= float(input("Enter the width of the rectangle: "))
#print(recLength)
#print(recWidth)
perimeter= 2*(recLength+recWidth)
print("The perimeter of a rectangle is:",perimeter)

area= recLength*recWidth
print("The area of a rectangle is:",area)