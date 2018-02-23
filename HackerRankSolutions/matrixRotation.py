#!/bin/python3
from copy import deepcopy
import sys
#https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
def matrixRotation(rows,columns,matrix):
    matrixs=[]
    new_r=r%(2*(rows+columns-2))#rotation limited to less than full rotation
    if rows-2>0 and columns-2>0:
        
        for matric in matrix[1:rows-1]:
            matrixs.append(matric[1:columns-1])#get the inner matrix
        
        remem=matrixRotation(rows-2,columns-2,matrixs)#get the inner matrix till reaching innermost
        
        matrix=addMatriceToMatrix(remem,matrix)#add transformed inner matrix to outer
        
    
    bosedk=transformed(traverseBoundaryClockwise(matrix),new_r,rows,columns,matrix)
    
    return bosedk
    
    
def addMatriceToMatrix(chhota,bada):#adds inner matrix to outer
    for i,i_dash in zip(range(1,(len(bada)-1)),range(0,len(chhota))):
        for j,j_dash in zip(range(1,len(bada[i])-1),range(0,len(chhota[i_dash]))):
            bada[i][j]=chhota[i_dash][j_dash]
    return bada
def traverseBoundaryClockwise(matrix):#converts boundary layer to linear matrix in counterclockwise tranverse
    a=[]
    for x in matrix:
        a.append(x[0])
        if x==matrix[-1]:
            for i in x[1:]:
                a.append(i)
    for x in matrix[-2:0:-1]:
        a.append(x[-1])
    for i in range(len(matrix[0])-1,0,-1):
        a.append(matrix[0][i])
   
    return a
    
def transformed(a,new_r,rows,columns,matrix):#converts linear matrix back to  boundary layer after transforming pos
    count=0
    
    b=deepcopy(matrix)
    
    for i in range(len(a)):
        new_i=i+new_r#new position of i after new_r rotations
        if(new_i>=len(a)):
            new_i-=len(a)#wraps around if greater than length of linear matrix
        if new_i<=(rows-1):#checks new position if leftboundary
            b[new_i][0]=deepcopy(a[i])
        elif new_i>(rows-1) and new_i<=(rows+columns-2):#checks new position if bottomboundary
            b[rows-1][new_i-rows+1]=deepcopy(a[i])
        elif new_i>(rows+columns-2) and new_i<=(len(a)-columns+1):#checks new position if rightboundary
            b[(rows-1)-(new_i-(rows+columns-2))][columns-1]=deepcopy(a[i])
        elif new_i>(len(a)-columns+1):#checks new position if top boundary
            b[0][len(a)-new_i]=deepcopy(a[i])
    
    return b
            
        
    
        
        
        
if __name__ == "__main__":
    global r
    m, n, r = input().strip().split(' ')
    m, n, r = [int(m), int(n), int(r)]
    matrix = []
    for matrix_i in range(m):
       matrix_t = [int(matrix_temp) for matrix_temp in input().strip().split(' ')]
       matrix.append(matrix_t)
    d=matrixRotation(m,n,matrix)
    print('\n'.join([' '.join(['{:n}'.format(item) for item in row]) 
      for row in d]))
     
