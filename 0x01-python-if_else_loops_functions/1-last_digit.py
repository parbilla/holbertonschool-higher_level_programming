#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
d = abs(number) % 10
if number < 0:
    d *= -1
if d > 5:
    print('Last digit of {:d} is {:d} and is greater than 5'.format(number, d))
elif d == 0:
    print('Last digit of {:d} is {:d} and is 0'.format(number, d))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, d))
