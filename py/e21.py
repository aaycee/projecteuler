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
    return sorted(amicable_numbers) # returns list

print(findAmicableNumbers(10000)) 
# [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368]
print(sum(findAmicableNumbers(10000))) # 31626, approx 0.020s runtime

