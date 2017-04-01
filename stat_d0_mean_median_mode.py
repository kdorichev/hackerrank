import numpy as np
import operator

N = input()
X = []
for i in range(1,N):
    X[i] = input()

print X

counts = {}
X = [ 'q1', 'q2', 'q2', 'q3', 'q3', 'q3', 'q4', 'q4', 'q4', 'q4'];
for i in X:
    counts[i] = counts.get(i,0)+1
print counts

counts_sorted = sorted(counts.items(), key=operator.itemgetter(1))
print counts_sorted[-1][0]
