# Akachukwu Obi
# Project Euler #25
# Solved Nov 30 2023

def fibonacciTerm(n = 1000):
    """ index of first Fibonacci term to contain n digits """
    a = b = 1 # first and second terms
    index = 2 # index of b
    while len(str(b)) < n:
        a, b = b, a + b
        index += 1
    return index
print(fibonacciTerm()) # 4782
