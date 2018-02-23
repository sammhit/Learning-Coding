#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/countingsort2/problem
def countingSort(arr):
    cArr = []
    finalArr = []
    for i in range(0,100):
        count=0
        for j in arr:
            if i==j:
                count+=1
        while count!=0:
            finalArr.append(i)
            count-=1
    
    return finalArr    
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))



