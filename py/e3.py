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

def isPrime(number = 6857):
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
        
# print(isPrime()) #True
# print(isPrime(2034921903459349123912734492132394813839123491293)) # False
print(isPrime(67280421310721)) # True

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