#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/electronics-shop/problem
def getMoneySpent(keyboards, drives, s):
    # Complete this function
    sarr=[]
    for keyboard in keyboards:
        for drive in drives:
            sarr.append(keyboard+drive)
    sarr.sort(reverse=True)
    
    for elem in range(len(sarr)):
        if s>=sarr[elem]:
            return sarr[elem]
        if elem==(len(sarr)-1):
            return -1
        




s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)

