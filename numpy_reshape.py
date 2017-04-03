import numpy as np
line = input()
arr = np.array(line.split())
new_arr = np.reshape(arr, [3,3])
print(new_arr)
