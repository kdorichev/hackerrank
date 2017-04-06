import numpy as np

(n,m) = map(int,input().split())

X = np.zeros((n,m), dtype=int)
for i in range(0,m):
    line = input()
    X[i] = line.split()

    print(np.mean(X,axis=1))
    print(np.var(X,axis=0))
    print(np.std(X))
