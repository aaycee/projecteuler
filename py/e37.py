# Akachukwu Obi
# Project Euler #37
# Solved Dec 4 2023

def truncateLeft(number):
    """ remove digits to the left of a number """
    num_str = str(number)
    return [int(num_str[i:]) for i in range(len(num_str))]

def truncateRight(number):
    """ remove digits to the right of a number """
    num_str = str(number)
    return [int(num_str[:-i]) for i in range(1, len(num_str))]

def isPrime(number):
    """ all primes greater than 3 are in the form of 6k +/- 1 
            where k is an integer """
    if number == 1:
        return False
    elif number < 4:
        return True # 2 and 3 are prime
    elif (number % 2 == 0) or (number % 3 == 0):
        return False
    elif number < 9: # just applies to 7 at this point
        return True
    else:
        factor = 5
        limit = int(number**0.5)
        while factor <= limit:
            if (number % factor == 0) or (number % (factor + 2) == 0):
                return False
            factor += 6
        return True # if no prime factor, n must be prime

def isTruncatablePrime(number):
    """ returns True or False if number is a truncatable prime """
    return all(isPrime(i) for i in truncateLeft(number) + truncateRight(number))

def findTruncatablePrimes(limit = 11):
    """ finds "limit" number of truncatable primes"""
    result = []
    num = 11  # Start with the first two-digit prime
    while len(result) < limit:
        if isPrime(num) and isTruncatablePrime(num):
            result.append(num)
        num += 2  # Skip even numbers
    return result
# print(sum(findTruncatablePrimes())) # 748317, 0.798 s

def primesSieve(limit = 2000000):
    """ finds prime numbers below some limit """
    sievebound = (limit) // 2 
    sieve = [False] * (sievebound) # initialize Boolean array to False
    divisorLimit = int(limit**0.5) // 2 
    for i in range(1, divisorLimit + 1):
        if not sieve[i]:
            p = 2*i + 1 # initial prime
            for j in range(i*(p+1), sievebound, p): # mark multiples of p
                sieve[j] = True
    primes = [2]  # 2 is prime
    primes += [2*i + 1 for i in range(1, sievebound) if not sieve[i]]
    return primes

def truncPrimesBelow(limit = 1000000):
    """ finds truncatable primes below some limit """
    primes = set(primesSieve(limit))
    truncPrimeSet = []
    for prime in primes:
        truncSet = truncateLeft(prime) + truncateRight(prime)
        if all(elem in primes for elem in truncSet): # check if it's a subset
            truncPrimeSet.append(prime)
    return set(truncPrimeSet) - {2, 3, 5, 7}
print(sum(truncPrimesBelow())) # 748317, 0.134 s

def isTruncatablePrime2(num, primes):
    num_str = str(num)
    for i in range(1, len(num_str)):
        left = int(num_str[i:])
        right = int(num_str[:-i])
        if left not in primes or right not in primes:
            return False
    return True

def truncatablePrimesSieve(limit = 1000000):
    primes = set(primesSieve(limit))
    result = [num for num in primes if isTruncatablePrime2(num, primes)]
    return set(result) - {2, 3, 5, 7}
print(sum(truncatablePrimesSieve())) # 748317, 0.0522s
