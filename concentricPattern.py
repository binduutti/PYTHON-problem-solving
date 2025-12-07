'''
Given an integer n, generate a square matrix of size (2n-1) x (2n-1) filled with concentric layers of integers from n down to 1.
For example, for n = 3, the output should be:
3 3 3 3 3
3 2 2 2 3
3 2 1 2 3
3 2 2 2 3
3 3 3 3 3
'''
n = int(input())

size = 2*n - 1
mat = [[0]*size for _ in range(size)]

left = 0
right = size - 1
top = 0
bottom = size - 1
num = n

while num > 0:
    for i in range(left, right+1):
        mat[top][i] = num
    
    for i in range(left, right+1):
        mat[bottom][i] = num
    
    for i in range(top, bottom+1):
        mat[i][left] = num
    
    for i in range(top, bottom+1):
        mat[i][right] = num
    
    left += 1
    right -= 1
    top += 1
    bottom -= 1
    num -= 1

for row in mat:
    print(*row) 
