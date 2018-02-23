#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/lisa-workbook/problem
def workbook(n, k, arr):
    pageNo = 1
    special = 0
    count = 0
    for i, j in zip(range(1,n+1), arr) :
        
        for problem in range(1,j+1):
            count+=1
            
            if pageNo == problem:
                special+=1
            if count>=k and problem!=j:
                pageNo+=1
                count=0
              
            
        pageNo+=1
        count=0
    return special      
    # Complete this function

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = workbook(n, k, arr)
    print(result)

