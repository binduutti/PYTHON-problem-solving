"""
Write a Python program that takes a list of integers as input on a single line
(separated by spaces), stores them in a list, and then calculates the sum of all
even numbers in the list.

Example:
Input:
Enter values of list: 1 2 3 4 5 6

Output:
Sum of even numbers in list: 12
"""
list = list(map(int,input("Enter values of list: ").split()))
sum=0

for i in range(len(list)):
    if list[i]%2==0:
        sum += list[i]
    
print("Sum of even numbers in list: ",sum)