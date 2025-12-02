'''
Write a Python program to convert minutes into hours and minutes.
e.g. 130 minutes = 2 hours and 10 minutes
'''
n=int(input("Enter minutes: "))
h=n//60
m=n%60
print(f"{h} hours,{m} minutes")