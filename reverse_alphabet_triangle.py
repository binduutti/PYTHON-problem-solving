'''
Write a Python program to print the reverse alphabet triangle pattern.
Sample Output:
E 
D E
C D E
B C D E
A B C D E
'''
n = int(input("Enter number:"))
start=65+n

for i in range(start,start-n,-1):
    for j in range(i,start+1):
        print(chr(j-1),end=" ")
    print()