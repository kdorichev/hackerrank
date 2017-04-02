"""
fd
"""
n  = int(input())

for i in range(0,n):
    line = input()
    pq = line.split()
#    print(pq[0], pq[1], pq[2], pq[3])
    px = int(pq[0])
    py = int(pq[1])
    qx = int(pq[2])
    qy = int(pq[3])
    rx = px + 2*(qx-px)
    ry = py + 2*(qy-py)
    print(rx, ry)


