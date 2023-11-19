#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:45:10 2023

@author: ac
"""

def sieveOfEratosthenes(limit = 7000):
    """returns prime numbers between 1 and limit"""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    p = 2 # starting from 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False # Mark multiples of p as non-prime
        p += 1
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    return primes

def factorsCount(number, primes):
    """ returns a 'prime factors: count' dictionary """
    factors = {} # initialize dict
    i = 0
    while primes[i] * primes[i] <= number:
        while number % primes[i] == 0:
            if primes[i] not in factors:
                factors[primes[i]] = 0 # initialize entry
            factors[primes[i]] += 1
            number //= primes[i]
        i += 1
    if number > 1:
        factors[number] = 1
    return factors

def triangleNumberWithDivisors(divisorLimit = 500):
    """ returns first triangle number with at least divisorLimit divisors """
    n = 1
    triangleNumber = 1
    while True:
        n += 1
        triangleNumber += n # iterative sum 
        primeFactors = factorsCount(triangleNumber, primes) 
        divisors = 1
        for count in primeFactors.values(): 
            divisors *= (count + 1) # formula for number of divisors
        if divisors > divisorLimit:
            return f"{triangleNumber}: {divisors} factors"

primes = sieveOfEratosthenes()
print(triangleNumberWithDivisors()) # 76576500, approx 0.0375 s

