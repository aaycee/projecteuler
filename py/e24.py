# Akachukwu Obi
# Project Euler 24
# Solved Nov 30 2023

def factorial(number):
    """ finds the factorial of any number """
    result = 1
    for i in range(0, number): # calculate factorial
        result = result * (number-i)
    return result

def nthPermutation(numOfDigits = 10, n = 10):
    """ returns the nth permutation of the range numOfDigits"""
    digits = list(range(numOfDigits)) # digits from 0 to 9
    permutation = []
    for i in range(numOfDigits-1, -1, -1): # iterate through digits in reverse
        fact = factorial(i) # get factorial
        index = (n - 1) // fact # calculate index
        permutation.append(digits.pop(index)) # add index digit to permutation
        n -= index * fact # Update the target permutation
    return ''.join(map(str, permutation)) # convert permutation list to a string

print(nthPermutation(10, 1000000)) # 2783915460