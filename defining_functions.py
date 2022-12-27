# 1.
sample_Input = [5, 3, 2, 10]


def mean(sample_Input):
    sum_SI = sum(sample_Input)
    length_SI = len(sample_Input)
    mean = sum_SI / length_SI
    print("The mean is", mean)
    return


mean(sample_Input)


# 2.
def isOdd(number):
    if type(number) == int:
        if number % 2 == 0:
            print("False")
            return False
        else:
            print("True")
            return True
    else:
        print("The input is not a number")


isOdd()


# 3.
def perimeter(length, width):
    result = length + width
    return result * 2


def main():
    answer = perimeter(3, 4)
    print(answer)


main()


# 4.
def interest(principal, rate, years):
    rate = rate/100
    new_balance = principal * (1 + (rate * years)) #ask here about return
    return new_balance


def main():
    tests = interest(100, 2, 5)
    print(tests)


main()



#5
def isRightTriangle(a, b, c):
    if (a > b) and (a > c):
        largest = a * a
        right = (b * b) + (c * c)
        return largest == right
    elif (b > a) and (b > c):
        largest = b * b
        right = (a * a) + (c * c)
        return largest == right
    else:
        largest = c * c
        right = (a * a) + (b * b)
        return largest == right


def main():
    checker = isRightTriangle(1, 2, 3)
    print(checker)

main()
