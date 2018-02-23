#!/bin/python3

import sys



def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = map(lambda x : x + a, apples)
    oranges = map(lambda x : x + b, oranges)
    countApples = 0
    countOranges = 0
    for apple in apples:
        if apple>=s and apple<=t:
            countApples+=1
    for orange in oranges:
        if orange>=s and orange<=t:
            countOranges+=1
    print(countApples) 
    print(countOranges)
    
    # Complete this function

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    countApplesAndOranges(s, t, a, b, apple, orange)
