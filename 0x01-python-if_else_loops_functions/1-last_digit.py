#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if digit > 5:
    condition = "and is greater than 5"
elif digit == 0:
    condition = "and is 0"
else:
    condition = "and is less than 6 and not 0"
print ("Last digit of", number, "is", digit, condition)
