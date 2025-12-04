'''
Write a program to print the following binary triangle pattern for a given number of rows.
For example, if the input number is 5, the output should be:
1
10
101
1010
10101
'''
n = int(input("Enter number: "))

for i in range(1, n+1):
    for j in range(i):
        if (i + j) % 2 == 1:
            print("1", end="")
        else:
            print("0", end="")
    print()
