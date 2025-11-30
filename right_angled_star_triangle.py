'''
Problem: Print a Right-Angled Star Triangle Pattern

Description:
Write a program that takes an integer input 'n' from the user and prints a right-angled triangle pattern of stars (*) 
with 'n' rows. Each row i (1 <= i <= n) should contain exactly i stars, separated by a space.

Input:
- An integer n (1 <= n <= 100), representing the number of rows of the triangle.

Output:
- A right-angled triangle of stars with 'n' rows.

Example:

Input:
5

Output:
* 
* * 
* * * 
* * * * 
* * * * * 
*
'''


n = int(input("Enter number:"))
for i in range(1,n+1):
    for j in range(0,i):
        print("* ",end=" ")
    print()
    