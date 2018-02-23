#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/the-birthday-bar/problem
def solve(n, s, d, m):
    count=0
        
    for i in range(n-m+1):
        if d == sum(s[i:i+m]):
            count+=1
    return count        
           
        
    # Complete this function

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)

