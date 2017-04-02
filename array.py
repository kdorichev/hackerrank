#!/bin/python3

import sys

n = int(input().strip())
file = list(map(int, input().strip().split(' ')))
#  Print the number of arrays defined in 'file' to STDOUT.
lines = 0
j=0
while j < n:
    j = j + file[j] + 1
        lines += 1
        print(lines)
