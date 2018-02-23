#!/bin/python3

import sys
import math
#https://www.hackerrank.com/challenges/flatland-space-stations/problem
def flatlandSpaceStations(n, c):
    maxd=0
   
    c= sorted(c)
    
    nfirst=abs(0-c[0])
    nlast=abs(n-1-c[-1])
    if nfirst >= nlast:
        maxd =nfirst
    else : maxd=nlast    
    for i in range(len(c)-1):
        hway= int(abs(c[i+1]-c[i])/2)
        if hway>maxd:
            maxd=hway
    return maxd        
           
    # Complete this function

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = list(map(int, input().strip().split(' ')))
    result = flatlandSpaceStations(n, c)
    print(result)

