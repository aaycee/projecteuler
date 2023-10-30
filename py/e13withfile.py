# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 09:39:12 2023

@author: AC
"""

def sumNumbersInFile(file_path='e13numbers.txt', n=10):
    """ open a file, sum numbers in the file, return first n digits"""
    try:
        with open(file_path, 'r') as file: # open file as read only
            numbers = [float(line.strip()) for line in file.readlines()]
            total = sum(numbers)
            firstNdigits = str(int(total))[:n]
            return firstNdigits
    except FileNotFoundError:
        return "File not found."
    except ValueError:
        return "Invalid data in the file."
print(sumNumbersInFile()) # 5537376230
print(sumNumbersInFile('e13numbers.txt', 52))
# 5537376230390876637302048746832985971773659831892672 (using int)
# 5537376230390877287140145935443224959721771787878400 (using float)


# decimal sum
from decimal import Decimal 

def sumNumbersInFileDec(file_path='e13numbers.txt', n=10):
    """ open a file, sum numbers in the file, return first n digits"""
    try:
        with open(file_path, 'r') as file: # open file as read only
            numbers = [Decimal(line.strip()) for line in file.readlines()]
            total = sum(numbers)
            return int(total)
    except FileNotFoundError:
        return "File not found."
    except ValueError:
        return "Invalid data in the file."
print(sumNumbersInFileDec()) # 5537376230
#5537376230390876637302048748000000000000000000000000

# manual decimal sum
def sumByColumn(file_path='e13numbers.txt'):
    """ transposes array of numbers in the file,
        then sums array by decimal manipulation"""
    try:
        with open(file_path, 'r') as file: # open file as read only
            numbers = [line.strip() for line in file.readlines()] # string
            numbersT = [list(row) for row in zip(*numbers)] 
            # transposes array to list of 50 lists 
            # containing 100 numbers as individual strings
            columnSums = []
            for i in numbersT: # go through transposed set
                columnSums.append(sum(float(j) for j in i)) # and sum each row
            total = 0
            count = 0
            limit = len(columnSums)
            while count < limit: # where the decimal part comes in
                total += (columnSums[limit-count-1]) * 10**count
                count += 1
            return int(total)
    except FileNotFoundError:
        return "File not found."
    except ValueError:
        return "Invalid data in the file."
    
print(sumByColumn()) 
# 5537376230390875957912150150527352055914711507533824

