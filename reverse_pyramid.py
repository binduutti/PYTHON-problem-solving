'''
Write a Python program to print the following reverse pyramid pattern using asterisks (*).
For example, if the input number is 5, the output should be:
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *  
        
'''

n=int(input())

for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for k in range((2*(n-i))-1):
        print("*",end=" ")
    print()