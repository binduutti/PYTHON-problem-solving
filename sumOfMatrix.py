'''
write a program to calculate the sum of all elements in a 2D matrix.
example:
Input:
1 2 3
4 5 6
Output:
21

'''
row_size = int(input("Enter the size of rows: "))
arr = []

for i in range(row_size):
    col_size = int(input(f"Enter the column size in row number {i}: "))
    
    while True:
        row = list(map(int, input(f"Enter {col_size} values: ").split()))
        
        if len(row) == col_size:
            arr.append(row)
            break
        else:
            print(f" Error: You must enter exactly {col_size} values.")
