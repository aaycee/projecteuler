# Akachukwu Obi
# Project Euler #38
# Solved Dec 21 2023

def spiralDiagonalSum(n = 1001):
    """ returns the sum of digonals of an n x n spiral grid"""
    m = n // 2
    return 1 + 2 * m * (8*m**2 + 15 * m + 13) // 3
# print(spiralDiagonalSum()) # 669171001

def spiralDiagonal(n=9):
    """ returns the sum of digonals of an n x n spiral grid """
    result = 1
    current = 1
    step = 2
    for _ in range(n//2):
        result += 4 * current + 10 * step
        current += 4 * step
        step += 2
    return result
print(spiralDiagonal()) # 669171001

def oddSquaresSum(n = 4):
    """ returns sum of squares of the first n odd numbers """
    return n * (4*n**2 - 1) // 3

def naturalNumSum(n = 10):
    """ returns sum of the first n natural numbers """
    return n * (n + 1) // 2

def spiralDiagSum(n = 1001):
    """ returns sum of diagonals of an n x n spiral grid """
    limit = n // 2
    return 1 + 4 * oddSquaresSum(limit) + 20 * naturalNumSum(limit)
print(spiralDiagSum()) # 669171001

def quadraticCoeffs(f1=3,f2=13,f3=31):
    a = (f3 - 2*f2 + f1) / 2
    b = f2 - f1 - 3*a
    c = f1 - a - b
    # return a, b, c
    return f"f(x) = {a}x^2 + {b}x + {c}"
# print(quadraticCoeffs(16, 60, 136)) # (4.0, -2.0, 1.0)

