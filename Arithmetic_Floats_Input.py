# Problem 1
# Prompt the user to enter a temperature in Farenheit, then convert it to Celsius
#and display the result.
# Display the result to 1 decimal places using an f-string format

user = int(input("Enter temperature in Farenheit: "))

celsius = ((user - 32) * 5/9)
print(f" The + {celsius:.1f} + vv")


# Problem 2
# Prompt the user to enter the length of side A, then side B of a right triangle.
#Calculate the
# length of the hypotenuse and display the result. Use the round() function to
#round the result to 1 decimal place

import math

userINPUT = float(input("Enter length of side A: "))
userINPUT2 = float(input("Enter length of B of a right triangle: "))

hypotenuse = (math.sqrt(userINPUT**2 + userINPUT2**2))

print(f"{hypotenuse:.1f}")


# Problem 3
# Prompt the user for their first name
# Display their name back to them, except with each letter in UPPERCASE

firstNAME = input("Enter your first name: ")

print(firstNAME.upper())


# Problem 4
# Prompt the user for the radius of a cirle, then calculate the area and
#circumference and display
# back to the user (no rounding or format necessary).  Be sure to use the math
#module's PI constant.

import math

radius = float(input("Enter the radius of the cirle: "))

circumference = ((2 * math.pi) * radius)

print(circumference)


# Problem 5
# Prompt the user to enter a (fake) credit card number.  It should be able to
#handle input like
# 123123412341234 and 1234-1234-1234-1234.  Display the last 4 numbers of the card
#back to the user.

enterCC = (input("Enter a fake credit card number (enter 12 numbers): "))

print(enterCC[-4:])
