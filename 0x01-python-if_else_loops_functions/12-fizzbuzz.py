#!/usr/bin/python3
def fizzbuzz(n):
    for num in range(1, n):
        if num % 3 == 0 and num % 5 != 0:
            print('Fizz', end=' ')
        elif num % 5 == 0 and num % 3 != 0:
            print('Buzz', end=' ')
        elif num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz', end=' ')
        else:
            print(num, end=' ')

n = 16

fizzbuzz(n)