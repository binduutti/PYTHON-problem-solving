'''
Program Name: Count_Even_Digits_in_String
Question:
Write a python program that reads a string from the user and counts how many
even digits (0, 2, 4, 6, 8) are present in the string. The program should check each
character using a suitable method (like Character.isDigit()) and finally
print the total number of even digits found in the input string.
'''
s = input("Enter String:")
count=0
for i in s:
    if i.isdigit():
        if int(i)%2 == 0:
            count += 1
print("count of digits in String: ",count)