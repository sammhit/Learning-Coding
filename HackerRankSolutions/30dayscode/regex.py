#!/bin/python3

import sys
import re

N = int(input().strip())
arr=[]
p=re.compile(r'@.+')
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    
    m=p.search(emailID)
    if (m.group()=='@gmail.com'):
        arr.append(firstName)
arr.sort()
for name in arr:
    print(name)
