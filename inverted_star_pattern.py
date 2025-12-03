'''Write a program to print the following pattern for a given number n.
For n = 5
* * * * *
* * * *
* * *
* *
*
'''
n = int(input("Enter number: "))

for i in range(1,n+1):
    for j in range(n+1,i,-1):
        print("*",end=" ")
    print()