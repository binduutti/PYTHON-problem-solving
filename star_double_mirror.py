'''
Write a Python program to print the star double mirror pattern.
Sample Output:
* * * * * * * * 
* * *     * * * 
* *         * * 
*             * 
*             * 
* *         * *
* * *     * * *
* * * * * * * *
'''
n=int(input("Enter number:"))

for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    for k in range(i*2):
        print(" ",end=" ")
    
    for l in range(i,n):
        print("*",end=" ")
    
    print()
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for k in range(2*(n-i-1)):
        print(" ",end=" ")
    
    for l in range(i+1):
        print("*",end=" ")
    
    print()
