#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/sock-merchant/problem
def sockMerchant(n, ar):
    total_socks=0
    for i in range(n-1):
        count=0
        for j in range(i+1,n):
            if ar[i]==ar[j]:
                count+=1
        if count%2!=0 and count!=0:
            total_socks+=1
    return total_socks        
    # Complete this function

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)

