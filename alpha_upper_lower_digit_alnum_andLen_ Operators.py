temp = float(input("Enter a temperature of water in fahrenheit."))

if 32 <= temp <= 212:
    print("The water is a liquid!")
elif temp > 212:
    print("The water is a gas!")
else:
    print("The water is a solid!")




letter = input("Enter in a letter, and I will tell you if it is a vowel or a consonant!")
letter = letter.upper()

if len(letter) > 1:
    print("Only enter one letter.")
elif letter.isalpha:
        if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
            print("You entered a vowel.")
        else:
            print("You entered a consonant!")
else:
    print("You didn't enter a letter!")




password = input("Enter in a random characters and numbers.")

if password.isalpha():
    print("Contains only letters.")
if password.isupper():
    print("Letters are uppercase letters.")
if password.islower():
    print("Letters are lowercase letters.")
if password.isdigit():
    print("Contains only digits.")
if password.isalnum():
    print("Contains only letters and digits.")
if password[-1]==".":
    print("the string ends with a period.")




diner_bill = float(input("Enter how much you spent at din-din!"))
diner_sat = input("Enter 1 for Totally satisfied, 2 for Satisfied, and 3 for Dissatisfied")

if diner_sat == str(1):
    diner_sat = (diner_bill * .20)
    print(diner_bill)
    print(f"You are totally satisfied with your meal! We would like you to tip ${diner_sat:.2f}.")

elif diner_sat == str(2):
    diner_sat = (diner_bill * .15)
    print(diner_bill)
    print(f"You are totally satisfied with your meal! We would like you to tip ${diner_sat:.2f}.")

elif diner_sat == str(3):
    diner_sat = (diner_bill * .20)
    print(diner_bill)
    print(f"You are totally satisfied with your meal! We would like you to tip ${diner_sat:.2f}.")
    exit()
else:
    print("Enter 1, 2, or 3.")




year = int(input('Enter an year: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year,'is a leap year.')
else:
    print(year, 'is not a leap year.')
