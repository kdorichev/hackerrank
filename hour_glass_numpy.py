""" https://www.hackerrank.com/challenges/30-2d-arrays
"""
# a - 2D array
# i,j - left corner (x) of hourglass shaped elements
# x b c
#   d 
# e f j

import numpy as np

def hourglass(a,i,j):
    summa  = a[j,j] + a[i,j+1] + a[i,j+2]
    summa += a[i+1,j+1]
    summa += a[i+2,j] + a[i+2,j+1] + a[i+2,j+2]
    return summa

a = np.zeros( (6,6), dtype=int)

for i in range(6):
    a[i] = input().split()
#print(a)

hourglasses = list()

for i in range(0,4):        # range of upper-left corner of hourglass shaped elements
    for j in range(0,4):
        hourglasses.append( hourglass(a,0,0) )

print( max(hourglasses) )


