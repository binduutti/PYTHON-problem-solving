'''
merge two arrays of strings
This program merges two arrays of strings into a single array.
It prompts the user to enter the size and elements of each array,
then combines them into a new array and prints the result.
Example:
Enter size of (String) array1:
4
Enter String values:
apple banana cherry date
Enter size of (String) array2:
5
Enter String values:
kiwi lemon mango orange pear
Merged array:
[apple, banana, cherry, date, kiwi, lemon, mango, orange, pear]
'''
n1 = int(input("Enter size of (String) array1: "))
arr1 = []
print("Enter String values:")
for _ in range(n1):
    arr1.append(input())

n2 = int(input("Enter size of (String) array2: "))
arr2 = []
print("Enter String values:")
for _ in range(n2):
    arr2.append(input())

merged_arr = arr1 + arr2

print(merged_arr)
