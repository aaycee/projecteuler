# Akachukwu Obi
# Project Euler #1
# created July 10, 2018

# solution 1 using a recursive function with memoization
def countRoutes(row, col, memo):
    """ counts paths in a row x col grid """
    if row == 0 or col == 0:
        return 1  # only one way to reach any cell in the first row or column
    if memo[row][col] > 0:
        return memo[row][col]
    # recursively sum the routes from the cell above and the cell to the left
    routes = countRoutes(row - 1, col, memo) + countRoutes(row, col - 1, memo)
    memo[row][col] = routes # memoize result to avoid redundant calculations
    return routes

def uniqueRoutes(row = 20, col = 20):
    """ tracks total unique paths in a row x col grid """
    # initialize memoization table with zeros
    memo = [[0] * (col + 1) for _ in range(row + 1)]
    return countRoutes(row, col, memo)  # start from the bottom-right corner
print(uniqueRoutes()) # 137846528820
print(uniqueRoutes(11, 25)) # 600805296


# solution 2 using an iterative walk


# solution 3 using combinatorics
from math import factorial

def latticePath(m=20, n=20):
    """ total unique paths in an m x n grid """
    return factorial(m + n) // (factorial(m)*factorial(n))
print(latticePath()) # 137846528820
print(latticePath(11, 25)) # 600805296


# solution 4 using multiplicative function
def latticePathSquareGrid(n=20):
    """ total unique paths in an n x n grid """
    result = 1
    for i in range(1, n+1):
        result = result * (n+i) // i
    return result
# print(latticePathSquareGrid()) # 137846528820