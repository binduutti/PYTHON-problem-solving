'''
Write a Python program to print the alphabet palindrome pyramid pattern.
Sample Output:
        A
      A B A
    A B C B A
  A B C D C B A
  
'''    
n = int(input("Enter Number: "))
start =65

for i in range(start,start+n):
    for j in range(i+1,start+n):
        print(" ",end=" ")
    for k in range(start,i+1):
        print(chr(k),end=" ")
    for l in range(i-1,start-1,-1):
        print(chr(l),end=" ")
print()