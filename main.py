'''
Write a program that demonstrates inheritance and constructor usage.

Create a base class A that stores an integer value x.

Initialize x using a constructor.

Create a derived class B that:

Inherits class A

Calls the parent constructor using super

Modifies the value of x by multiplying it by 2

Prints the updated value of x

Take input from the user and create an object of class B.

Example:
Input: 5
Output: 10
'''
class A:
    def __init__(self, x):
        self.x = x


class B(A):
    def double(self):
        print(self.x * 2)


x = int(input("Enter number: "))

obj = B(x)
obj.double()