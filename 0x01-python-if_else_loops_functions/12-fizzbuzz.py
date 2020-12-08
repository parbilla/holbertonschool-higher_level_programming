#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            var = 'FizzBuzz'
        elif i % 5 == 0:
            var = 'Buzz'
        elif i % 3 == 0:
            var = 'Fizz'
        else:
            var = i
        print('{} '.format(var), end='')
