'''
Write a Python program to add two matrices entered by the user.
Matrix 1:
1 2 3
4 5 6

Matrix 2:
7 8 9
1 2 3

Output Matrix:
8 10 12
5 7 9

'''
# Matrix 1 input
n = int(input("Enter number of rows in mat1: "))
m = int(input("Enter number of columns in mat1: "))
mat1 = []

for i in range(n):
    row = []
    print(f"Enter {m} values for row {i+1}:")
    while len(row) < m:
        row.extend(map(int, input().split()))
    mat1.append(row[:m])

print("Matrix 1:")
for row in mat1:
    print(*row)

# Matrix 2 input
k = int(input("Enter number of rows in mat2: "))
l = int(input("Enter number of columns in mat2: "))
mat2 = []

for i in range(k):
    row = []
    print(f"Enter {l} values for row {i+1}:")
    while len(row) < l:
        row.extend(map(int, input().split()))
    mat2.append(row[:l])

print("Matrix 2:")
for row in mat2:
    print(*row)

if n != k or m != l:
    print("Matrix addition not possible (dimensions mismatch)")
else:
    output = []

    for i in range(n):
        row = []
        for j in range(m):
            row.append(mat1[i][j] + mat2[i][j])
        output.append(row)

    print("Output Matrix:")
    for row in output:
        print(*row)
