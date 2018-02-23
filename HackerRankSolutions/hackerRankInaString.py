#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem
def hackerrankInString(s):
    # Complete this function
    comp = list("hackerrank")
    head=0;
    for ch in s:
        if ch==(comp[head]):
            head+=1
            if head == 10:
                return "YES"
            
    return "NO"

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)

