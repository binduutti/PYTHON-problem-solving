"""
❓ QUESTION:

Write a Python program to:

1. Ask the user to enter the size of a list.
2. Read 'n' integer values into the list.
3. Compute the sum of all elements.
4. Create a function that returns "even" if the sum is even,
   otherwise returns "odd".
5. Print the total sum and whether it is even or odd.

Example:
Input:
Enter size of array: 5
Enter 5 values:
1 2 3 4 5

Output:
The sum of array is 15 and it is odd
"""
list = list(map(int,input().split()))

sum=0

for i in list:
    sum += list[i]
    
if sum%2==0:
    print("sum of list is even")
else:
    print("sum of list is odd")