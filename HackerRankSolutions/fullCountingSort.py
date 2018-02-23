#!/bin/python3

import sys
from collections import defaultdict
#https://www.hackerrank.com/challenges/countingsort4/problem

if __name__ == "__main__":
    xDict = defaultdict(list)
    
    n = int(input().strip())
    for a0 in range(n):
        x, s = input().strip().split(' ')
        x, s = [int(x), str(s)]
        if a0<n/2:
            xDict[x].append("-")
        else:
            xDict[x].append(s)
    for x,s in xDict.items():
        print (" ".join(s),end=' ')
            
      
    
    
    

