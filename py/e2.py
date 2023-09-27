# Akachukwu Obi, edited Sep 27, 2023
# Project Euler #2 - sum of even fibonacci terms
# see js file for build up and explanation

""" .js code
function evenFibonacciSum(limit) {
    "use strict";
    var a, b, c, sum;
    a = 1;
    b = 1;
    c = a + b;
    sum = 0;
    while (c < limit) {
        sum += c; // only adding c, which are even
        a = b + c; // classic fibonacci algorithm
        b = a + c;
        c = a + b;
    }
    return sum;
}
// test
evenFibonacciSum(4000000);
"""

def euler2(n):
    """
    sum of even Fibonacci numbers less than n (n = 4000000)
        using lessons from euler1

    """
    fibSet = [1,2]
    while fibSet[-1] < n:
        fibSet += [fibSet[-1] + fibSet[-2]]
    # print(fibSet)
    return (sum([i for i in fibSet if i % 2 == 0])) # sum of even-valued terms
  
print(euler2(4000000)) # solution is 4613732

def euler2(n):
    """
    sum of even Fibonacci numbers less than n (n = 4000000)

    """
    fibSet = [1,2] # initiate the Fibonacci set
    total = 2
    while fibSet[-1] < n: 
        fibSet += [fibSet[-1] + fibSet[-2]] # create new member from the last two digits
        if fibSet[-1] % 2 == 0:
            total += fibSet[-1] # sum even-valued terms
    # print(fibSet)
    return total
    
print(euler2(4000000)) # solution is 4613732


def evenFibonacciSum(limit):
    """
    sum of even Fibonacci numbers less than n (n = 4000000)
        for a more elegant solution, consider the fibonacci sequence
        1,1,2,3,5,8,13,21,34...
        a,b,c,a,b,c,a,b,c...
        every even number falls on c; and after the first a and b,
        c = a+b; a = c+b and b = a+c
    
    """
    a = 1 # first term
    b = 1 # second term
    c = a + b # third term
    total = 0
    
    while c < limit:
        total += c # only adding c which are even
        a = b + c # classic fibonacci algorithm
        b = a + c
        c = a + b
        
    return total

# test
print(evenFibonacciSum(4000000)) # 4613732