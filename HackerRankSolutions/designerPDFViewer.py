#!/bin/python3

import sys
#https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
def designerPdfViewer(h, word):
    new_word=word.lower()
    arr=[]
    farr=[]
    
    for i in range(len(new_word)):
        arr.append(ord(new_word[i]))
    for i in arr:
        for j in range(len(h)):
            if i-97==j:
                farr.append(h[j])
                break
    
    return max(farr)*len(farr)

    # Complete this function

if __name__ == "__main__":
    h = list(map(int, input().strip().split(' ')))
    word = input().strip()
    result = designerPdfViewer(h, word)
    print(result)

