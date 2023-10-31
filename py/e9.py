# Akachukwu Obi, 2018
# Project Euler #9

# Solution 1 based on definition of pythagorean triplets
def pythagoreanTripleSum(upTo=1000):
    """find pythagorean triplet a+b+c = upTo, return a*b*c if found"""
    for a in range(3, (upTo - 3) // 3):
        for b in range(a + 1, (upTo - a) // 2):
            c = upTo - b - a
            if c * c == (a * a) + (b * b):
                # return a * b * c
                return str(a) + ' * ' + str(b) + ' * ' + str(c) + ' = ' + str(a * b * c)
    return "I toiled all night and found nothing"
print(pythagoreanTripleSum()) # 200 * 375 * 425 = 31875000
print(pythagoreanTripleSum(237)) # I toiled all night and found nothing

#solution 1b modifed for multiples 
from math import sqrt
def pythagoreanTripleSum(upTo=1000):
    """find pythagorean triplet a+b+c = upTo, return a*b*c if found"""
    for a in range(3, (upTo - 3) // 3):
        for b in range(a + 1, (upTo - a) // 2):
            c = sqrt((a * a) + (b * b))
            if c == int(c): # if c is a rational number
                c = int(c)
                S = a + b + c
                if S == upTo:
                    return f"{a} * {b} * {c} = {a * b * c}"
                elif upTo % S == 0:
                    k = upTo // S
                    return f"{k*a} * {k*b} * {k*c} = {k**3 * a * b * c}"
    return "I toiled all night and found nothing"
print(pythagoreanTripleSum()) # 200 * 375 * 425 = 31875000


# Solution 2 using parameterization
import math

def pythagoreanTripletSumTo(total=1000):
    """find pythagorean triplet a+b+c = total, return a*b*c if found
        script based on the parametrization of pythagorean triplets"""
    mlimit = int(math.sqrt(total/2)) + 1
    for m in range(2, mlimit): # starts at 2 to ensure nrange is a range
        if m % 2 == 0: # if even
            nrange = range(1, m, 2) # make n odd
        else:
            nrange = range(2, m, 2) # else make n even
        for n in nrange:
            # formula below always gives a,b,c as pythagorean triplets
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2 
            if a + b + c == total:
                return f"{a} * {b} * {c} = {a * b * c}"
            elif total % (a + b + c) == 0: # checks for non primitive sets
                k = total // (a + b + c)
                return f"{k*a} * {k*b} * {k*c} = {k**3 * a * b * c}"
    return "I toiled all night and found nothing"

print(pythagoreanTripletSumTo()) # 375 * 200 * 425 = 31875000
print(pythagoreanTripletSumTo(200)) # 75 * 40 * 85 = 255000
# total = 200 returns "I toiled..." without the elif script