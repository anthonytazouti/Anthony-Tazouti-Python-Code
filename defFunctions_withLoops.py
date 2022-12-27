#1
def isPalindrome(word):
    if word[::-1] == word:
        print("True")
    else:
        print("False")


def main():
    word = input("Enter in a word: ")
    isPalindrome(word)


main()


#2
def isValidPassword(password):
    containsDigit = False
    containsLower = False
    containsUpper = False
    containsAN = False
    length = False

    for x in password:
        if x.isdigit():
            containsDigit = True
        if x.islower():
            containsLower = True
        if x.isupper():
            containsUpper = True
        if not x.isalpha():
            containsAN = True
        if len(password) == 8:
            length = True

    if containsAN and containsLower and containsUpper and containsDigit and length:
        print("True")
    else:
        print("False")


def main():
    password = input("Enter in a password: ")
    isValidPassword(password)


main()

# 3
import math


def Circumference(radius):
    result = math.pi * radius ** 2
    return result


answer = Circumference(2)
print(answer)


# 4
import random
def printValues():
    l = 0
    num = list()

    while l < 5:
        num.append(random.randint(1, 69))
        l += 1
    num.sort()

    print(num)

printValues()


# 5
def printlist():
    trees = ["ash", "bradford pear", "cedar", "dogwood", "elm", "fir", "gingko", "hickory"]

    for i in range(8):
        print(trees[i])
    trees.insert(0, "aspen")
    trees.pop(1)

    print("*"*20)

    count = 0
    while count < 8:
        print(trees[count])
        count += 1


printlist()
