'''
    Write a program to reverse a given integer number.

    The program should:
        - Take an integer input from the user.
        - Extract each digit from the number.
        - Construct the reversed number by appending digits in reverse order.
        - Print the reversed number as output.

    Example:
        Input:  12345
        Output: 54321

        Input: 907
        Output: 709
'''
n = int(input("Enter integer:"))
rev = ""
while n>0:
    rev += str(n%10)
    n=n//10
print(rev)