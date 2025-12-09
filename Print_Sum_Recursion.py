'''
Write a recursive function to calculate the sum of first N natural numbers.
e.g., if N = 3, the output should be:
1 + 2 + 3 = 6
'''
def sum(n):
    if n<1:
        return 0
    return n+sum(n-1)

print(sum(int(input("Enter Number: "))))
