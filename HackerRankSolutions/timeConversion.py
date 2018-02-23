#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    if s[-2:]=="PM" and s[:2]!='12':
        return str(int (s[0:2])+12)+s[2:-2]
    elif s[0:2]=='12' and s[-2:]=='AM':
        return ("00"+s[2:-2])
        
    else:
        return s[:-2]
        
        

s = input().strip()
result = timeConversion(s)
print(result)
