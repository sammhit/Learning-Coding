#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/insertionsort2/problem
def insertionSort2(n, arr):
    for index in range(1,len(arr)):

        currentvalue = arr[index]
        position = index

        while position>0 and arr[position-1]>currentvalue:
            arr[position]=arr[position-1]
            position = position-1

        arr[position]=currentvalue
        print(" ".join(map(str,arr)))        
          
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)

