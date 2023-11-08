#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 08:30:17 2023

@author: ac
"""
    
def generate_pascals_triangle(n=10):
    """ generate pascal's triangle up to n rows"""
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle # returns a list of lists

def display_pascals_triangle(triangle):
    """ display pascal's triangle with left padding """
    max_width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        num_spaces = max_width - len(" ".join(map(str, row)))
        left_padding = " " * (num_spaces // 2)
        row_str = " ".join(map(str, row))
        print(left_padding + row_str)

# Specify the number of rows you want in Pascal's Triangle
n = 10
pascals_triangle = generate_pascals_triangle(n)
display_pascals_triangle(pascals_triangle)
