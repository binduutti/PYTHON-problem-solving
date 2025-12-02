'''
Write a Python program to remove all occurrences of a specific element from a list.
'''
list = list(map(int,input("Enter list: ").split()))

n = int(input("Enter number to eliminate: "))

for i in list:
    if i==n:
        list.remove(i)

print(list)