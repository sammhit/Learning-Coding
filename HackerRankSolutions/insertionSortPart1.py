#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/insertionsort1/problem
def insertionSort1(n, arr):
    elem=arr[-1]
    for i in range(len(arr)-1,-1,-1):
        if elem >arr[i-1]:
            arr[i]=elem
            break
        elif elem<arr[0] and i==0:
            arr[0]=elem
            break
        else:
            arr[i]=arr[i-1]
        print(" ".join(map(str,arr)))
    print(" ".join(map(str,arr)))
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort1(n, arr)

