'''
Write a Python program to display the reverse alphabet triangle pattern.
Input Number: 6
Expected Output:
A
AB
ABC
ABCD
ABCDE
ABCDEF

'''
n = int(input("Enter number: "))
start = 65
for i in range(n, 0, -1):     
    for j in range(start, start + i):
        print(chr(j), end="")
    print()
