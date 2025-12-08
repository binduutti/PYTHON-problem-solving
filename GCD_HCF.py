
'''write a java program to find GCD or HCF of two numbers and also count total number of divisors of GCD or HCF.
example:
Input: num1=12, num2=15
Output: GCD or HCF=3, Total divisors=2 (1,3)'''
n1=int(input("Enter number1: "))
n2=int(input("Enter number2: "))
divisors = 0
list=[]
for i in range(1,n1):
    if n1%i==0 and n2%i==0:
        divisors += 1 
        list.append(i)
print(divisors)
print(list)