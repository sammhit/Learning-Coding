#!/bin/python3

import sys
import collections
#https://www.hackerrank.com/challenges/game-of-thrones/problem
def gameOfThrones(s):
    freqs=collections.Counter(s)
    countOdd=0
    countEven=0
    for value in freqs.values():
        if value%2==0:
            countEven+=1
        elif value%2!=0:
            countOdd+=1
            
    if countOdd==1:
        return "YES"
    elif countEven==len(freqs):
        return "YES"
    else:
        return "NO"
        
    # Complete this function

s = input().strip()
result = gameOfThrones(s)
print(result)

