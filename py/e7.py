# Akachukwu Obi
# Project Euler #7 

# see .js files for build up

from math import sqrt

def isPrime(number):
    """determines if number is prime"""
    if number == 1:
        return False
    elif number < 4:
        return True 
    elif (number % 2 == 0) or (number % 3 == 0):
        return False
    elif number < 9:
        return True
    else:
        factor = 5
        limit = int(sqrt(number))
        while factor <= limit:
            if (number % factor == 0) or (number % (factor + 2) == 0):
                return False
            factor += 6
        return True # if no prime factor, n must be prime

def nthPrime(n = 10001):
    """finds the nth prime"""
    primeSet = [2]
    count = 1
    while len(primeSet) < n:
        count += 2
        if isPrime(count):
            primeSet.append(count)
    return primeSet[-1]

print(nthPrime()) # 104743

def nthPrimeSieve(n = 10001):
    """uses a sieve to find the nth prime"""
    primes = [2]
    num = 3

    while len(primes) < n:
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 2

    return primes[-1]

print(nthPrimeSieve()) # 104743