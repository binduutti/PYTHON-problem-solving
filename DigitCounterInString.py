'''
Question:
Write a python program that reads a string from the user and counts how many 
digits (0–9) are present in the string. The program should check each 
character using a suitable method (like Character.isDigit()) and finally 
print the total number of digits found in the input string.
'''
s = input("Enter String:")
count=0
for i in s:
    if i.isdigit():
        count += 1
print("count of digits in String: ",count)