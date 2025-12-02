'''
Write a python program to check whether a given number is a prime number.

The program should:
1. Ask the user to enter a number.
2. Determine whether the number is prime.
   - A prime number is a number greater than 1 that has no divisors 
     other than 1 and itself.
3. Print:
   - true or false (indicating prime status)
   - A message: "yes its a prime number" or "no its not a prime number"

Example:
Input:
Enter number:
7

Output:
true
yes its a prime number

'''
n = int(input("Enter number: "))
prime = True
if n<2:
    prime = False

for i in range(2,n):
    if(n%i == 0):
        prime = False

if prime:
    print("yes its a prime number")
else:
    print("no its not a prime number")