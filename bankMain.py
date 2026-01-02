'''
Write a program to simulate basic bank account operations.

Create a class BankAccount with:

An instance variable balance

A constructor to initialize the balance

Implement methods:

deposit(amount) → adds money to balance

withdrawal(amount) → subtracts money only if sufficient balance exists

In the main program:

Take user input for:

Initial balance

Deposit amount

Withdrawal amount

Perform deposit and withdrawal operations

Print the final account balance

example:
Input: 1000 500 200
Output: 1300

'''

class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    
    def deposit(self,amt):
        self.balance += amt
    
    def withdrawl(self,amt):
        if self.balance > amt :
            self.balance -= amt
b,d,w = map(int,input().split())

obj = BankAccount(b)
obj.deposit(d)
obj.withdrawl(w)

print(obj.balance)