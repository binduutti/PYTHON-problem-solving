'''
Write a Python program to print the star bowtie pattern.
Sample Output:
*             * 
* *         * *
* * *     * * *
* * * * * * * *
* * *     * * *
* *         * *
*             *
'''
n = int(input("Enter number: "))

for i in range(1, n):
    for j in range(i):
        print("*", end=" ")
    for k in range(2 * (n - i)):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(1, n + 1):
    for j in range(i, n + 1):
        print("*", end=" ")
    for k in range(2 * i - 2):
        print(" ", end=" ")
    for j in range(i, n + 1):
        print("*", end=" ")
    print()
