#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/runningtime/problem
def runningTime(l):
    count=0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            j -= 1
            count+=1
        l[j+1] = key
       
    return count   

    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = runningTime(arr)
    print(result)

