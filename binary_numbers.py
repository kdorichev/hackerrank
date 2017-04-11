"""
 1 <= n <= 10**6
 2**20 > 1048576 -- 20 bit max required to represent 10**6

"""
n = int(input())

# Find most meaningful bit m in binary form
m = 0
for i in range(20,-1,-1):
     if n - 2**(i) >= 0:
         m = i   # m bits starting from 0
         break
print("{} bits are required to represent {}".format(m+1,n) )

binary_str = list()
# Fill the binary string with bits
for i in range(m,-1,-1):
   if n - 2**(i) >= 0:  # i-th bit is raised
        binary_str.append(1) 
        n -= 2**(i)     # decrease on value of the i-th bit
   else:                # i-th bit is not raised
        binary_str.append(0) 

print(binary_str)
#find most long sequense of consequtive '1' bits
maxi = 0
curr = 0
for i in range(len(binary_str)):
    if binary_str[i] == 1:
        curr += 1
    else: # 0
        if curr > maxi:
            maxi = curr
        curr = 0 # new sequence, counter restart

if curr > maxi:
    maxi = curr
print(maxi)
