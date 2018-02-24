#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/quicksort3/problem

def quicksort(arr,low,high):
    
    if low<high:
        p = partition(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)
    


def partition(arr,low,high):
    pivot=arr[high]
    j=low-1
    for i in range(low,high):
        if arr[i]<pivot:
            j+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            
    temp=arr[j+1]
    arr[j+1]=arr[high]
    arr[high]=temp     
    print(" ".join(map(str,arr)))
    return j+1        


    

if __name__=="__main__":
    n=int(input().strip())
    arr=list(map(int,input().strip().split(' ')))
    result = quicksort(arr,0,n-1)
