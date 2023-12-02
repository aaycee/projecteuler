#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 00:21:20 2023

@author: ac
"""

def sumOfDivisors(number = 50):
    """ Returns the sum of proper divisors of a number """
    total = 1  # Start with 1 since every number is divisible by 1
    if number % 2 == 0:
        total += 2
        total += number // 2
        step = 1
    else:
        step = 2 # odd numbers only have odd divisors
    for i in range(3, int(number**0.5) + 1, step):
        if number % i == 0:
            total += i
            if i != number // i:
                total += number // i
    return total

def findAmicableNumbers(limit = 1000):
    """ returns amicable numbers less than limit """
    amicable_numbers = set() # initialize dictionary
    for a in range(2, limit):
        b = sumOfDivisors(a)
        if b > a and sumOfDivisors(b) == a:
            amicable_numbers.add(a)
            amicable_numbers.add(b)
    return sum(amicable_numbers)

print(findAmicableNumbers(10000)) # 31626, approx 0.020s runtime

# alternative, condensed version
def getDivisorsForRange(limit=1000):
    """ gets divisors for a range of numbers """
    divisorsSum = {}
    for num in range(2, limit + 1):
        divisors = [i for i in range(1, int(num**0.5) + 1) if num % i == 0]
        divisors += [num // i for i in divisors if i != num // i]
        divisorsSum[num] = sum(divisors) - num
    return divisorsSum

def findAmicableNumbersfromSet(limit=1000):
    """ finds sum of amicable numbers less than some limit"""
    amicableNumbers = set()
    divisorsSum = getDivisorsForRange(limit)
    for number, item in divisorsSum.items():
        if number < item < limit and number == divisorsSum[item]:
            amicableNumbers.add(number)
            amicableNumbers.add(item)
    return sum(amicableNumbers)

print(findAmicableNumbersfromSet(10000)) # 31626, 0.020 s runtime
