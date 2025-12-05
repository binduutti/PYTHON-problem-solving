'''
Write a Python program to print the following number palindrome gap pattern up to n rows.
Input Number: 5
Expected Output:
    1             1
    1 2         2 1
    1 2 3     3 2 1
    1 2 3 4 4 3 2 1
    
'''
n = int(input("Enter number: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range((2 * (n - i))):
        print("_", end=" ")

    for j in range(i, 0, -1):
        print(j, end=" ")

    print()