#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/kangaroo/problem
def kangaroo(x1, v1, x2, v2):
    
    while (x2>=x1 and v2<v1) or (x2<=x1 and v2>=v1):
            if v1==v2 and (x1>x2 or x2>x1):
                break
            if x1!=x2:
                x1=x1+v1
                x2=x2+v2
            else:
                return "YES"
    return "NO"
    
    # Complete this function

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
