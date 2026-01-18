#Write a program that draws two random combinations of numbers for a combination lock:
#a 3-digit code where each number is between 0 and 9.
#b 4-digit code where each number is between 1 and 6.

import random

#a 3-digit code where each number is between 0 and 9.

number1 = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
number2 = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"

print(number1)
print(number2)


##b 4-digit code where each number is between 1 and 6.
digit1=f"{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}"
digit2=f"{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}"
print(digit1)
print(digit2)
