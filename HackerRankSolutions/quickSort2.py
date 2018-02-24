#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/quicksort2/problem

def quicksort(arr):
    
    pivot = arr[0]
    left=[]
    right=[]
    for elem in arr:
        if elem<pivot:
            left.append(elem)
        elif elem>pivot:
            right.append(elem)
    if len(left)>1:
        left=quicksort(left)
    if len(right)>1:
        right=quicksort(right)
    left.append(pivot)
    print(" ".join(map(str,left+right)))
    return left+right



if __name__=="__main__":
    n = int(input().strip())
    arr=list(map(int,input().strip().split(' ')))
    result =quicksort(arr)
    
