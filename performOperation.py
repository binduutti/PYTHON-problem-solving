'''
PerformOperation
     This program performs basic arithmetic operations based on user input.
     It takes two integers and an operator as input and outputs the result.
    example:
     Enter number1:
     10
     Enter number2:
     5
     Enter Operation:
     +
     Output:
     15
'''

a = int(input("Enter a: "))
b = int(input("Enter b: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b if b != 0 else "Division by zero")
    case _:
        print("Invalid operator")
