'''
Write a Python program to print the following alphabet pattern up to n rows.
Sample Output:
A
BB
CCC
DDDD
EEEEE

'''

n = int(input("Enter number: "))

start = 65

for i in range(start,start+n):
    for j in range(start,i+1):
        print(chr(i),end="")
    print()
    