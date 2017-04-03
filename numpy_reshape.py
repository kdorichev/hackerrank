import numpy as np
# Input a string, split onto numbers and convert into integers
arr = np.array(input().split(), dtype=int)
# Create a re-shaped array
new_arr = np.reshape(arr, [3,3])
print(new_arr)
