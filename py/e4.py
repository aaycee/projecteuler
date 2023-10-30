# Akachukwu Obi, edited Oct 23, 2023
# Project Euler #4 - Largest Palindrome Number


# Solution 1: factorization

import math

def getThreeDigitMultiples(number = 580085):
    """returns 3-digit multiples of a number"""
    factors = []
    possibleFactor = 1
    limit = math.sqrt(number)
    
    while possibleFactor <= limit:
        if number % possibleFactor == 0: # if it is a factor
            factors.append(possibleFactor)
            otherPossibleFactor = number // possibleFactor
            if otherPossibleFactor != possibleFactor:
                factors.append(otherPossibleFactor)
        possibleFactor += 1
        
    threeDigitMultiples = []
    for i in factors:
        if len(str(i)) == 3 & len(str(number // i)) == 3:
            threeDigitMultiples.append(i)
    
    return sorted(threeDigitMultiples) # sorts the set 
# print(getThreeDigitMultiples()) # [583, 995]

def isPalindrome(number):
    """returns true if number reads the same forwards and backwards"""
    num_str = str(number) # converts number to string
    return num_str == num_str[::-1]

def checkPalindromeMultiple():
    """returns largest palindrome number with two 3-digit multiples"""
    for i in range(998001, 10000, -1):
        if isPalindrome(i) and len(getThreeDigitMultiples(i)) != 0:
            return i
        
print(checkPalindromeMultiple()) #906609
# took 0.015s runtime


# Solution 2: using python's string reverse check 

def isPalindrome(number):
    """returns true if number reads the same forwards and backwards"""
    num_str = str(number) # converts number to string
    return num_str == num_str[::-1]

def largestPalindromeProduct():
    """find largest palindrome product of two 3-digit numbers"""
    max_product = 0
    for i in range(999, 99, -1): # count backwards
        for j in range(i, 99, -1): # starting j from i avoids duplicates
            product = i * j
            if product <= max_product:
                break # leave inner loop once we find max value
            if isPalindrome(product):
                max_product = product # update max value
    return max_product

print(largestPalindromeProduct()) # 906609
# took 0.00075 s

# Solution 2 updated for divisibility by 11
def isPalindrome(number):
    """returns true if number reads the same forwards and backwards"""
    num_str = str(number) # converts number to string
    return num_str == num_str[::-1]

def largestPalindromeProduct():
    """find largest palindrome product of two 3-digit numbers
        every even-digited palindrome is divisible by 11 """
    max_product = 0
    for i in range(999, 99, -1): # count backwards
        if i % 11 != 0: # focus initial values on multiples of 11
            continue
        for j in range(999, i-1, -1): 
            product = i * j
            if product <= max_product:
                break # leave inner loop once we find max value
            if isPalindrome(product):
                max_product = product # update max value
    return max_product

print(largestPalindromeProduct()) # 906609
# took 7.32e-05 s