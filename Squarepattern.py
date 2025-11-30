
"""
Write a Python program to print an n x n square pattern using asterisks (*).

Input:
A single integer n.

Output:
An n x n square where each row contains n stars.

Example:
Input:
4

Output:
* * * *
* * * *
* * * *
* * * *
"""
n = int(input("Enter number:"))

for i in range(n):
    for j in range(n):
        print("* ",end=" ")
    
    print()
    
