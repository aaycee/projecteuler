# Akachukwu Obi, 2018
# Project Euler #10

# all variations of the Sieve of Eratosthenes

def sieveEratosthenes(limit = 2000000):
    """ finds prime numbers below some limit"""
    is_prime = [True] * (limit + 1) # initialize boolean list to True
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    p = 2 # start counter at 2
    while p * p <= limit:
        if is_prime[p]: # If is_prime[p] is still True
            for i in range(p * p, limit + 1, p): # multiples of p
                is_prime[i] = False # are not prims
        p += 1 # increment counter 
    primes = [p for p in range(2, limit + 1) if is_prime[p]] # curate primes
    return primes

print(sum(sieveEratosthenes())) # 142913828922, takes 0.105 s


def primesLessThan(limit = 2000000):
    """ sums prime numbers less than some limit """
    halfLimit = (limit-1) // 2 # 
    a = [True]*halfLimit # initialize boolean
    divisorLimit = int(limit**0.5) // 2
    for i in range(divisorLimit):
        if a[i]: # if True
            p = 2*i + 3 # initial prime 2i + 3
            j = i + p # a[j] is composite; i + 2i + 3 = 3(i + 1)
            while j < halfLimit: # mark False
                a[j] = False
                j += p # multiples of p
    primes = [2]
    primes += [2*i + 3 for i in range(halfLimit) if a[i]]
    return primes

print(sum(primesLessThan())) # 142913828922; took 0.0511 s


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
print(sum(primesSieve())) # 142913828922, takes approx 0.0445 s






