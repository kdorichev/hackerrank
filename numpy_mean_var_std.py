import numpy as np
# Read n,m -- two integers from 1st line -- matrix's dimensions
(n,m) = map(int,input().split()) # Split the string and convert into integer each number with int()

X = np.zeros((n,m), dtype=int)  # create a 2D zero matrix of integer type values
for i in range(0,m):            # For each of m rows
    line = input()              # read next row
    X[i] = line.split()         # Split and assign; conversion into integer -- implicitly by numpy

    print(np.mean(X,axis=1))    # Calculate mean per each column
    print(np.var(X,axis=0))     # Calculate variance per each row
    print(np.std(X))            # Calculate standard deviation for flattened matrix -- all the elements
