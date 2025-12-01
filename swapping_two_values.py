'''
Write a  program to swap the values of two numbers using a temporary
variable.

The program should:
1. Ask the user to enter the first number.
2. Ask the user to enter the second number.
3. Swap the values of the two numbers using a temporary variable.
4. Print the values of number1 and number2 after swapping.

Example:
Input:
number1 = 5
number2 = 9

Output:
number1 val: 9
number2 val: 5

'''
n1 = int(input("Enter number1:"))
n2 = int(input("Enter number2:"))

n1,n2 = n2,n1

print (f"n1: {n1},n2: {n2}")