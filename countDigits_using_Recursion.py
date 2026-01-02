'''Count the number of digits in a given number using recursion.'''

n = int(input("Enter number:"))

def count(n):
    if n==1 or n==0:
        return 1
    return 1+count(n//10)

print(count(n))