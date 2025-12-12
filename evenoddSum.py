'''
Write a program to check if the sum of even numbers is equal to the sum of odd numbers in a given list of integers.
e.g.
Input: [1, 2, 3, 4, 5, 6]
Output: True
'''

s=input("Enter input: ").strip().strip("[]")

listt = list(map(int,s.split(",")))
sum1=0
sum2=0

for i in range(len(listt)):
    if listt[i]%2==0:
        sum1 += listt[i]
    else:
        sum2 += listt[i]

print("True" if sum1==sum2 else "False")

