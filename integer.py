# 4. Write a program that asks the user for three integer numbers.
# The program prints out the sum, product, and average of the numbers.

number1=float(input("Enter the number1: "))
number2=float(input("Enter the number2: "))
number3=float(input("Enter the number3: "))

#print(number1)
#print(number2)
#print(number3)

#sum of the numbers
sum= number1+number2+number3
print("The sum is:",sum)

#product of the numbers
product=number1*number2*number3
print("The product is:",product)

#average of the numbers
average= sum/3
print("The average is:",average)

