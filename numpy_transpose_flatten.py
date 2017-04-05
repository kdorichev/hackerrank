"""
You are given a N x M integer array matrix with space separated elements ( N = rows and M = columns). 
Your task is to print the transpose and flatten results.
"""

import numpy as np

(N,M) = map(int,input().split())

array = np.fromfunction(input().split(),(N,M),dtype=int)

#array = np.zeros( (N,M) )

line = ""

for i in range(0,N):
    line = input()
    array = np.vstack(array,line)

print(array)
