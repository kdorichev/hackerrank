import numpy as np

n,m = map(int,input().split())

a = np.zeros((n,m), dtype=int)
for i in range(n):
    row = input()
    a[i] = row.split()

b = np.zeros((n,m), dtype=int)
for i in range(n):
    row = input()
    b[i] = row.split()

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

