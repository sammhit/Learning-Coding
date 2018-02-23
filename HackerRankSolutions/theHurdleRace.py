#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/the-hurdle-race/problem
def hurdleRace(k, height):
    # Complete this function
    h_max=max(height)
    if h_max<=k:
        return 0
    else:
        return h_max-k

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = list(map(int, input().strip().split(' ')))
    result = hurdleRace(k, height)
    print(result)

