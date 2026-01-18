# 5 Write a program that asks the user to enter a mass in medieval units:
# talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user:
#
# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.


talent= float(input("Enter the talent: "))
pound= float(input("Enter the pound: "))
lots= int(input("Enter the number of lots: "))

#then we can convert everything to grams
talent_grams=talent*20*32*13.3
pound_grams=pound*32*13.3
lots_grams=lots*13.3

#print(talent_grams)
#print(pound_grams)
#print(lots_grams)

total_grams=talent_grams+pound_grams+lots_grams
print("The total gram is:",total_grams)



