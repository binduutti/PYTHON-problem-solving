'''
write a program to calculate the factorial of a number using recursion.
example:
Input: 5
Output: 120
'''

def fact(n):
    if n<2:
        return 1
    return n*fact(n-1)
n = int(input("Enter number:"))
print(fact(n))