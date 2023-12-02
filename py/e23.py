# Akachukwu Obi
# Project Euler #23 - Abundant Sums
# solved Nov 26, 2023

def getDivisors(number):
    """ get proper divisors of any number """
    divisors = [1]
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            divisors.extend([i,number//i])
    return list(set(divisors))

def getAbundantNumbers(limit):
    """ get abundant numbers up to limit """
    abundantNums = []
    for i in range(12, limit):
        if sum(getDivisors(i)) > i:
            abundantNums.append(i)
    return abundantNums

def nonAbundantSumsSet(limit = 28123):
    """ returns integers that cannot be expressed 
            as sum of abundant numbers """
    abundantNums = getAbundantNumbers(limit)
    abundantNumSums = set()
    for i in range(len(abundantNums)):
        for j in range(i, len(abundantNums)):
            candidate = abundantNums[i] + abundantNums[j]
            if candidate <= limit:
                abundantNumSums.add(candidate)
            else: break # stops inner loop once sum exceeds limit
    nonAbundantNumSums = set(range(1, limit + 1)) - abundantNumSums
    return nonAbundantNumSums

print(sum(nonAbundantSumsSet())) # 4179871, took 0.591 s


def nonAbundantSumsBelow(limit = 28123):
    """ returns integers that cannot be expressed 
            as sum of abundant numbers """
    abundantNums = getAbundantNumbers(limit)
    nonAbundantNums = [i for i in range(limit)]
    for i in range(len(abundantNums)):
        for j in range(i, limit):
            candidate = abundantNums[i] + abundantNums[j]
            if candidate < limit:
                nonAbundantNums[candidate] = 0
            else: break # stops inner loop once sum exceeds limit
    return nonAbundantNums

print(sum(nonAbundantSumsBelow())) # 4179871, takes 0.446 s