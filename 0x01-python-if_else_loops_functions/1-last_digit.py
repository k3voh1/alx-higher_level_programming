#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = repr(number)
lastDigitStr = number_string[-1]
lastDigit = int(lastDigitStr)
if number > 0:
    print("Last digit of", number, "is", lastDigit, end=" ")
    if lastDigit > 5:
        print("and is greater than 5")
    elif lastDigit == 0:
        print("and is 0")
    else:
        print("and is less than 6 and not 0")
else:
    print("Last digit of", number, "is", -lastDigit, end=" ")
    if lastDigit == 0:
        print("and is 0")
    else:
        print("and is less than 6 and not 0")
