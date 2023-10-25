# Akachukwu Obi, 2018
# Project Euler #3 - Largest Prime Factor


# I have 3 possible solutions

# Sol 1: computes the factors of the number then seives those factors for primality

import math

def getFactors(number=128):
	factors = []
	possibleFactor = 1
	limit = math.sqrt(number)
	while possibleFactor <= limit: # we only need to check to the square root
		if number % possibleFactor == 0: # if it is a factor
			factors.append(possibleFactor) # add it to factors
			otherPossibleFactor = number // possibleFactor 
			if otherPossibleFactor != possibleFactor:
				factors.append(otherPossibleFactor)
		possibleFactor += 1
	return sorted(factors)
# test
# print(getFactors(128))

def getPrimeFactors(number=128):
    factors = getFactors(number) # returns a set of factors
    primeFactors = []
    if len(factors) == 2:
        primeFactors = [number]
    else:
        if 2 in factors:
            primeFactors += [2]
        for i in factors: 
            if (i % 2 != 0) and len(getFactors(i)) == 2:
                primeFactors.append(i)
    
    # return primeFactors # returns set of prime factors
    return primeFactors[-1] # return largest prime factor
# test
print(getPrimeFactors()) # 2
print(getPrimeFactors(600851475143)) # 6857

# Solution 2: using a different primality test

def isPrime(n):
	if n == 1:
		return False
	elif n < 4:
		return True # 2 and 3 are prime
	elif (n % 2 == 0) or (n % 3 == 0): # a single '|' or 'or' could represent 'or'
		return False
	elif n < 9: # just applies to 7 at this point
		return True
	else:
		f = 5
		r = math.floor(math.sqrt(n))
		while f <= r:
			if (n % f == 0) or (n % (f + 2) == 0):
				return False
			f += 6 # all primes greater than 3 are in the form of 6k +/- 1 where k is an integer

		return True # if there is no prime factor less than sqrt(n), then n must be prime

def getPrimeFac(number):
	a = getFactors(number)
	if isPrime(number):
		return number;
	else:
		primeFactors = [];
		for i in a: # loop through every element in a
			if isPrime(i): # every prime number has exactly 2 factors only
				primeFactors.append(i)

		# return primeFactors
		return primeFactors[-1] # return largest prime factor

# print(getPrimeFac(101)) # 101
print(getPrimeFac(600851475143)) # 6857

import math

def primeFactors(number = 600851475143):
    """
    takes a number and returns its prime factorization
    """
    factorSet = []
    
    # while even ...
    while number % 2 == 0:
        factorSet.append(2)
        number = number // 2
         
    # while odd ...
    for i in range(3, int(math.sqrt(number))+1 , 2):
        while number % i== 0:
            factorSet.append(i),
            number = number // i
             
    # if number remains prime > 2 after all, print it
    if number > 2:
        factorSet.append(number)
    
    return factorSet # returns prime factorization    
# test
prime_factors = primeFactors()
print(primes_factors) # [71, 839, 1471, 6857]
print(primes_factors[-1]) # 6857 