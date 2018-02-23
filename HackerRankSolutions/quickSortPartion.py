#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/quicksort1/problem

def quickSort(arr):
    pivot = arr[0]
    left = []
    right = []
    for i in arr:
        if i>pivot:
            right.append(i)
        if i<pivot:
            left.append(i)
    left.append(pivot)
    return left+right
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = quickSort(arr)
    print (" ".join(map(str, result)))



