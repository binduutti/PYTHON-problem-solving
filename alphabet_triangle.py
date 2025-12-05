
'''
write a Python program to print the following alphabet triangle pattern up to n rows.
Input Number: 6
Expected Output:
A 
A B
A B C
A B C D
A B C D E
'''

n = int(input("Enter number: "))
start = 65  
for i in range(start, start + n):
    for j in range(start, i + 1):
        print(chr(j), end=" ")
    print()