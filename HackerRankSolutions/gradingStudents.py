#!/bin/python3

import sys
import math

def solve(grades):
    for i,grade in enumerate(grades):
        if grade>=38:
            if grade%5>=3:
                grades[i] = math.ceil(grade/5)*5
   
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
