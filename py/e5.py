# Akachukwu Obi
# Euler 5, edited Oct 24, 2023

# Solution 1a, prime factorization using Sieve of Eratosthenes
def sieveOfEratosthenes(limit):
    """returns prime numbers between 1 and limit"""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False # Mark all multiples of p as non-prime
        p += 1
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    return primes

def smallestMultiple(limit = 20):
    """returns smallest multiple divisible by integers 1 to limit"""
    primes = sieveOfEratosthenes(limit) # gets set of primes in the range
    result = 1 
    for prime in primes:
        power = 1
        while prime ** power <= limit: # will run at least once all primes
            power += 1
        result *= prime ** (power - 1) 
    return result
print(smallestMultiple()) # 232792560

# time check for much larger ranges
import time
start = time.time()
smallestMultiple(200000) # don't print, value exceeds 4300 digit limit
end = time.time()
print(end - start) # approx 0.142 s

# Solution 1b, prime factorization without Sieve of Eratosthenes
import math

def smallest_multiple(n = 20):
    """returns smallest multiple divisible by integers 1 to n"""
    prime_factors = {} # dictionary
    for i in range(2, n + 1):
        factors = {}
        num = i
        
        # find prime factors of the current number
        for j in range(2, int(math.sqrt(num)) + 1):
            while num % j == 0:
                num //= j
                factors[j] = factors.get(j, 0) + 1
        if num > 1:
            factors[num] = factors.get(num, 0) + 1
            
        # update max count of prime factors
        for factor, count in factors.items():
            prime_factors[factor] = max(prime_factors.get(factor, 0), count)
   
    # calculate lcm from the set of prime factors
    result = 1
    for factor, count in prime_factors.items():
        result *= factor ** count

    return result

print(smallest_multiple()) # 232792560
# smallest_multiple(200000) took approx 1.29 s

# Solution #2a without using gcd or lcm from the math module
def gcd(x, y):
	"""find the greatest common divisor of any two numbers"""
	while y != 0:
		result = x % y
		x = y # reassign values
		y = result # ensures we eventually get x % y == 0
	return x

def lcm(a, b):
	return (a * b) // gcd(a, b)

def smallestNumDivBy(low = 1, high = 20):
	result = low
	for i in range(low, high + 1):
		result = lcm(result, i) # lcm of previous lcm and next number
	return result
print(smallestNumDivBy()) # 232792560
# smallestNumDivBy(1, 200000) took approx 9.22 s

# Solution #2b using gcd available in most Python versions
from math import gcd
def lowestCommonMultiple(n = 20):
    """finds lcm for the range of numbers 1 to n"""
    result = 1
    for i in range(1, n + 1):
        result = result * i // gcd(result, i) # calculates lcm
    return result
# test
print(lowestCommonMultiple()) # 232792560
# lowestCommonMultiple(200000) took approx 9.22 s

# Solution 3 using both gcd and lcm avalilable in Python 3.9 and later
from math import lcm
numbers = [i for i in range(1,21)]
print (lcm(*numbers)) # 232792560
# time check for range(1,200001) is also approx 9.22 s

