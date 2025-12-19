'''
write a program to set the entire row and column to 0 if an element is 0 in a matrix.
example:
Input:
1 1 1
1 0 1
1 1 1

Output:
1 0 1
0 0 0
1 0 1
'''
n = int(input("Enter rows: "))
m = int(input("Enter columns: "))
mat = []
for i in range(n):
    row = []
    print(f"Enter {m} values in row {i}")
    while len(row)<m:
        row.extend(list(map(int,input().split())))
    row = row[:m]
    mat.append(row)

print("The original matrix: ")
for i in mat:
    print(*i)
zero_rows = set()
zero_columns=set()

for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            zero_rows.add(i)
            zero_columns.add(j)

for i in zero_rows:
    for j in range(m):
        mat[i][j] =0
        
for i in zero_columns:
    for j in range(n):
        mat[j][i]=0

print()
print("The matrix after modifying zeroes: ")
for i in mat:
    print(*i)