'''
Write a program to print the half diamond pattern as shown below:
For example, if the input number is 5, the output should be:
*
* *
* * *
* * * * 
* * * * *
* * * *
* * * 
* *
*
'''

n=int(input("Enter number:"))

for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(2,n+1):
    for j in range(n+1,i,-1):
        print("*",end=" ")
    print()