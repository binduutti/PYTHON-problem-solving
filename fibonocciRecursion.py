'''
write a program to find nth Fibonacci number using recursion.
example:
Input: 6
Output: 8
'''
n = int(input("Enter Number:"))

def fibanocci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibanocci(n-1)+fibanocci(n-2)

print(fibanocci(n))