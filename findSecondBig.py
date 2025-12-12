'''
Write a program to find the second greatest among three numbers.
e.g.
Input: 3 7 5
Output: 5
'''
a, b, c = map(int, input("Enter 3 numbers: ").split())

if (a > b and a < c) or (a > c and a < b):
    print("a is second greatest")
elif (b > a and b < c) or (b > c and b < a):
    print("b is second greatest")
else:
    print("c is second greatest")