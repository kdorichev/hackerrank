'''
https://www.hackerrank.com/challenges/30-2d-arrays
'''
def hourglass(a,i,j):
    summa  = a[i][j] + a[i][j+1] + a[i][j+2]
    summa += a[i+1][j+1]
    summa += a[i+2][j] + a[i+2][j+1] + a[i+2][j+2]
    return summa

a = [ [0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0],
      [0,0,0,0,0,0] ]

row = list()
for i in range(6):
    row = input().split()
    for j in range(6):
        a[i][j] = int(row[j])

#print(a)

hourglasses = list()

for i in range(0,4):
    for j in range(0,4):
        hourglasses.append( hourglass(a,i,j) )

print( max(hourglasses) )


