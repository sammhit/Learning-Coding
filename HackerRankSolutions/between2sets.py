#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/between-two-sets/problem
def getTotalX(a, b):
    count=0
    
    
    max_a=max(a)
    min_b=min(b)
    arr=[]
    final_arr=[]
    for j in range(max_a,int(min_b/2)+1):
        count_a=0
        for i in a:
            if j%i==0:
                count_a=count_a+1
        if count_a==len(a):
            arr.append(j)
    for elem in arr:
        count_b=0
        for j in b:
             if j%elem==0:
                count_b+=1
        if count_b==len(b):
            final_arr.append(elem)
                
    for j in b:
        if (j%min_b!=0):
            count=count+1
    if count==0:
        for i in a:
            if(min_b%i!=0):
                count=count+1
    if count==0:
        final_arr.append(min_b)
            
                    
    return len(final_arr)

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)

