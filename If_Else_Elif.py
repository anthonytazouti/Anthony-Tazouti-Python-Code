#1. Write a program that reads three numbers and prints if they
#are all the same
#or prints "not all the same" if not.

user = float(input("Enter in a number:"))
user2 = float(input("Enter in another number:"))
user3 = float(input("Enter in one more number:"))

if user == user2 == user3:
    print("You enterd 3 numbers that are the same!")
else:
    print("All three numbers you entered are not the same!")

#2. Write a program that asks the user for their birth year, then
#calculate their age (just using the
#difference between 2022 and their birthyear.  Then determine
#if they are old enough to vote (18).
#If they can vote, tell them so.  If not, tell them how many
#years until they can vote.  Make sure you test
#someone who is less than 18, 18, and someone older than 18

currentYear = 2022
birthYear = int(input("What is your birth year?"))
userAge = currentYear - birthYear

if birthYear <= 2004:
    print("You are old enough to vote!")
else:
    yearsUntil = 18 - userAge
    print("You will be old enough to vote in " + str(yearsUntil) + " year/s")

#3. Write a program to simulate a bank transaction.
#There are two bank accounts: checking and savings.
#First, ask for the initial balances of the bank accounts;
#reject negative balances.
#Then ask for the transaction; options are deposit or
#withdrawal
#Then ask for the account; options are checking and savings.
#Then ask for the amount; reject transactions that overdraw an account.
#At the end, print the balances of both accounts.

Balcheck = float(input("Enter in your balance for your checking account."))
Balsav = float(input("Enter in your balance for your savings account."))

if Balcheck < 0 or Balsav < 0:
    print("No negative balances are allowed!")
else:
    transType = input("Are you making a deposit a withdrawl?").upper()
    accountType = input("Savings or Checking?").upper()

    if transType == "DEPOSIT":
        depositAmt = (float(input("How much do you want to deposit?")))
        if depositAmt < 0:
            print("Deposit must be > 0!")
        else:
            if accountType == "SAVINGS":
                Balsav = (Balsav + depositAmt)
            elif accountType == "CHECKING":
                Balcheck = (Balcheck + depositAmt)
            else:
                print("Invalid entry!")

    elif transType == "WITHDRAWL":
        withdrawlAmt = (float(input("How much money do you want to take out?")))
        if withdrawlAmt < 0:
            print("Withdrawl must be > 0!")
        else:
            if accountType == "SAVINGS":
                if withdrawlAmt > Balsav:
                    print("You can't take that much out!")
                else:
                    Balsav = (Balsav - withdrawlAmt)
            elif accountType == "CHECKING":
                if withdrawlAmt > Balcheck:
                    print("You can't take that much out!")
                else:
                    Balcheck = (Balcheck - withdrawlAmt)
            else:
                print("You can't take that much out!")
    else:
        print("Invalid account type!")

    print("Your savings account balance is $" + str(Balsav))
    print("Your checking account balance is $" + str(Balcheck))

#4. A supermarket awards coupons depending on how much a customer
#spends on groceries.
#For example, if you spend $50, you will get a coupon worth
#eight percent of that amount
#Table 1 (in Canvas) shows the percent used to calculate the
#coupon awarded for different amounts spent.
#Write a program that calculates and prints the value of the
#coupon a person can receive based on groceries purchased

#Money Spent in dollars	Coupon Percentage
#Less than 10	No coupon
#From 10 to 60	8 %
#More than 60 to 150	10%
#More than 150 to 210	12%
#More than 210	14%

userSpends = float(input("Enter how much you spent!: "))

if userSpends > 210:
    discountRec = (userSpends * .14)
    print(f"The coupon you can receive based on how much you spent is worth ${discountRec:.2f}!")
elif userSpends > 150 < 210:
    discountRec = (userSpends * .12)
    print(f"The coupon you can receive based on how much you spent is worth ${discountRec:.2f}!")
elif userSpends > 60 < 150:
    discountRec = (userSpends * .10)
    print(f"The coupon you can receive based on how much you spent is worth ${discountRec:.2f}!")
elif userSpends > 10 < 60:
    discountRec = (userSpends * .08)
    print(f"The coupon you can receive based on how much you spent is worth ${discountRec:.2f}!")
else:
    print("You did not spend enough to receive a coupon discount! Spend more!")

#5.Write a program that translates a % in a class to a letter
#grade.  Use the grade ranges found in
#Table 2 (in Canvas).  Prompt the user for their % and tell
#them their letter grade.

userPrctg = float(input("Enter in your percentage that you earned in class, and I'll convert it to a letter grade!"))

if userPrctg >= 93 <= 100:
    print("Your grade translates to an A!")
elif userPrctg >= 90 <= 92:
    print("Your grade translates to a A-!")
elif userPrctg >= 87 <= 89:
    print("Your grade translates to a B+!")
elif userPrctg >= 83 <= 86:
    print("Your grade translates to a B!")
elif userPrctg >= 80 <= 82:
    print("Your grade translates to a B-!")
elif userPrctg >= 77 <= 79:
    print("Your grade translates to a C+!")
elif userPrctg >= 73 <= 76:
    print("Your grade translates to a C!")
elif userPrctg >= 70 <= 72:
    print("Your grade translates to a C-!")
elif userPrctg >= 67 <= 69:
    print("Your grade translates to a D+!")
elif userPrctg >= 63 <= 66:
    print("Your grade translates to a D!")
elif userPrctg >= 60 <= 62:
    print("Your grade translates to a D-!")
elif userPrctg < 60:
    print("Your grade translates to a F!")
else:
    print("You did not enter a numerical value!")
