# Akachukwu Obi, 2018
# Project Euler #6

# see .js file for build up

def diffSums(limit = 100):
    """finds the difference between sum of squares 
    and square of sums of natural numbers"""
    sums = limit * (limit + 1) // 2
    sumOfSquares = limit * (limit + 1) * (2*limit + 1) // 6
    return sums**2 - sumOfSquares

print(diffSums()) # 25164150