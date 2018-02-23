#!/bin/python3

import sys
import collections
#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
def isValid(s):
    freqs=collections.Counter(s)
    count=0
    countValue=0
    mark=list(freqs.values())[0]
    for value in freqs.values():
        if value==mark:
            count+=1
    if count==len(freqs):
        return "YES"
    freqs2= collections.Counter(list(freqs.values()))
    valuesList=list(freqs2.values())
    anchor=max(valuesList)
    anchorkey=list(freqs2.keys())[list(freqs2.values()).index(anchor)]
    for key in freqs2.keys():
        if int(key)==int(anchorkey)+1 and int(freqs2[key])==1:
            countValue+=1
        elif int(key)==1 and int(freqs2[key])==1:
            countValue+=1
    if countValue==1:
        return "YES"
    
    return "NO"
    # Complete this function

s = input().strip()
result = isValid(s)
print(result)

