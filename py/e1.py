# Akachukwu Obi
# Project Euler #1
# edited Sep 27, 2023

def Multi35(count):
	# no need to initialize variables
	count = count - 1
	m3 = 3 * 0.5 * (count // 3) * ((count // 3) + 1) # // works as math.floor in both python2.7 and python3
	m5 = 5 * 0.5 * (count // 5) * ((count // 5) + 1) 
	m15 = 15 * 0.5 * (count // 15) * ((count // 15) + 1)
	return int(m3 + m5 - m15) # would have been returned as a float int() converts to whole number int
	
print(Multi35(1000)) # solution 233168

# another strategy is to make multiplication formula it's own function

def euler1(n=1000, a=3, b = 5):
    """
    sum of multiples of a or b in range(1,n)
        euler1() runs with the default values n=1000, a=3, b = 5
        otherwise can accept up to three integer inputs

    """
    n = n-1 # comment out to include upper range
    
    def sumMultiplesOfNum(i):
        return i*0.5*(n//i)*((n//i) + 1)
    
    return int(sumMultiplesOfNum(a) + sumMultiplesOfNum(b) - sumMultiplesOfNum(a*b))

# tests
print(euler1()) # solution 233168
print(euler1(1000)) # solution 233168
print(euler1(1000, 3, 5)) # solution 233168
print(euler1(10**10)) # solution 23333333331666665472