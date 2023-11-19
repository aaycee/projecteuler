# Akachukwu Obi
# Project Euler #1
# created July 10, 2018

# solution 1
def getFactors(number=128):
    """ gets factors of any number """
    factors = []
    possibleFactor = 1
    limit = number ** 0.5
    while possibleFactor <= limit: 
        if number % possibleFactor == 0: 
            factors.append(possibleFactor) 
            otherPossibleFactor = number // possibleFactor 
            if otherPossibleFactor != possibleFactor:
                factors.append(otherPossibleFactor)
        possibleFactor += 1
    return sorted(factors)

def triangleNumber(factorlength=10):
    """ returns triangle number with minimum factorlength factors"""
    n = 1 # position of triangle number
    triNum = n * (n + 1) // 2
    factorset = getFactors(triNum)
    while len(factorset) <= factorlength:
        n += 1
        # triNum = n * (n + 1) // 2 # formula for triangle numbers
        triNum += n # iterative sum for triangle numbers
        factorset = getFactors(triNum)
    return f"{triNum}: {len(factorset)} factors"
    # return f"{n}th triangle number is {triNum} with {len(factorset)} factors"
# print(triangleNumber(500)) # 76576500: 576 factors
# runtime is approx 2.04 s

# solution 2, consolidates
def triangleNumberwith(divisorLimit = 500):
    n = 1 # position of triangle number
    triangleNumber = 1
    
    while True:
        n += 1
        triangleNumber += n # iterative sum
        divisors = 0
        for i in range(1, int(triangleNumber**0.5) + 1): # find and count  factors
            if triangleNumber % i == 0:
                divisors += 2  # counts both i and triangle_number // i
        if divisors > divisorLimit:
            return triangleNumber   
# print(triangleNumberwith()) # 76576500, 1.34 s runtime

def primeFactorsCount(number):
    """ returns a 'prime factors: count' dictionary """
    factors = {} # initialize dict
    i = 2 # first prime number
    while i * i <= number:
        while number % i == 0:
            if i not in factors:
                factors[i] = 0 # initialize entry
            factors[i] += 1
            number //= i
        i += 1
    if number > 1:
        factors[number] = 1
    return factors
print(primeFactorsCount(2500)) # {2: 2, 5: 4}

def triangleNumberWithDivisors(divisorLimit = 500):
    """ returns first triangle number with at least divisorLimit divisors """
    n = 1
    triangleNumber = 1
    while True:
        n += 1
        triangleNumber += n # iterative sum 
        primeFactors = primeFactorsCount(triangleNumber) 
        divisors = 1
        for count in primeFactors.values(): 
            divisors *= (count + 1) # formula for number of divisors
        if divisors > divisorLimit:
            return f"{triangleNumber}: {divisors} factors"
print(triangleNumberWithDivisors()) # 76576500: 576 factors, 0.124 s runtime