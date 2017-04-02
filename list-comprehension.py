"""
You are given three integers  and  representing the dimensions of a cuboid along with an integer . You have to print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, 

Input Format

Four integers  and  each on four separate lines, respectively.

Constraints

Print the list in lexicographic increasing order.

Sample Input

1
1
1
2
Sample Output

[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]] 
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    coord = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k != n]
    print(coord)

