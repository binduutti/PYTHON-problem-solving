'''
Write a Python program to print the diamond pattern using stars (*).
For example, if the input number is 5, the output should be:
        *  
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

'''
n=int(input("Enter number:"))

for i in range(n-1):
    for j in range(i,n-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range((2*(n-i))-1):
        print("*",end=" ")
    print()