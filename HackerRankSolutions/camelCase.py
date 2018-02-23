#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/camelcase/problem    

def camelcase(s):
    count=1
    for ch in s:
        
        if ord(ch)>=65 and ord(ch)<=91:
             count+=1
    return count
    # Complete this function

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)

