'''
    Write a program to check whether a given number is an Armstrong number.

    A number is called an Armstrong number if the sum of its digits, 
    each raised to the power of the total number of digits, 
    is equal to the original number.
    
    Examples:
        Input: 153
        Explanation: 1^3 + 5^3 + 3^3 = 153  → Armstrong Number

        Input: 370
        Explanation: 3^3 + 7^3 + 0^3 = 370  → Armstrong Number

        Input: 123
        Explanation: 1^3 + 2^3 + 3^3 = 36 ≠ 123  → Not Armstrong

    Task:
        - Take an integer input from the user.
        - Check if it is an Armstrong number.
        - Print "Yes" if it is Armstrong, otherwise print "No".
'''
n = int(input("Enter integer:"))
sum=0
length = int(len(str(n)))
temp = n
while n>0:
    num = n%10
    sum += num ** length
    n=n//10
if sum==temp:
    print("Yes its a Armstrong Number")
else:
    print("No its not a Armstrong Number")
    
    