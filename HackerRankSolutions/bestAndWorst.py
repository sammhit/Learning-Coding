#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
def breakingRecords(score):
    hRecords = 0
    lRecords = 0
    highest = score[0]
    lowest = score[0]
    for each in score:
            if each>highest:
                hRecords+=1
                highest=each
            if each<lowest:
                lRecords+=1
                lowest=each
    return hRecords, lRecords
                
                
        
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))
