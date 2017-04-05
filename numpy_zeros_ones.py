import numpy as np

args = map(int,input().split()) # Unknown number of indices --> list
indices = list(args)

print( np.zeros(indices, dtype = np.int) )
print( np.ones (indices, dtype = np.int) )
