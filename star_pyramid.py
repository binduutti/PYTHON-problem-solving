'''
Write a Python program to print a star pyramid pattern based on user input.
For example, for n = 5, the output should be:
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
n = int(input("Enter number: "))

for i in range(0,n):
    for j in range(n-1,i,-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()