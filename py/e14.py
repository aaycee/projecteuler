# Akachukwu Obi
# Project Euler #14 - Longest Collatz sequence (phi function)
# Solved July 22, 2018

def phiFunction(number):
	""" generates a Collatz sequence given a starting number"""
	result = [number]
	while number > 1:
		if number % 2 == 0:
			number = number // 2
		else:
			number = 3 * number + 1
		result.append(number)
	return result
# print(phiFunction(16))

# just focusing on length using recursion
def lenPhiSet(number):
    """returns length of a Collatz sequence starting at number"""
    if number == 1:
        return number
    elif number % 2 == 0:
        return 1 + lenPhiSet(number // 2)
    else:
        return 1 + lenPhiSet(3*number + 1)
print(lenPhiSet(16))

def longestChainUnder(number):
	""" find the longest collatz sequence under a given number limit """
	maxLength = 0
	for i in range(number//2 + 1, number, 2): # assuming number would be odd
		length = len(phiFunction(i))
		if length > maxLength:
			maxLength = length
			result = i
	return str(result) + ": " + str(maxLength) + " members"
print(longestChainUnder(1000000)) # 837799: 525 members; finished in 11.6 s


""" with several useful optimizations, we can shorten calculation time """
