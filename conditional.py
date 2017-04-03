#!/bin/python3
import sys

N = int(input().strip())
isWeird = False
#print N

if N % 2 != 0: # odd
    isWeird = True
else:
    if N in range(2,6) or N>20:
        isWeird = False
    elif N in range(6,21):
        isWeird = True

print("Weird") if isWeird else print("Not Weird")

