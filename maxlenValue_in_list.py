'''
write a program to find the longest string in a list of strings.
example: input: ["apple", "banana", "cherry", "date"]
'''
listt = input("Enter Strings: ").split()

maxlen = 0
maxlenindex = 0
maxlenvalue = ""

for i in range(len(listt)):
    if len(listt[i]) > maxlen:
        maxlen = len(listt[i])
        maxlenindex = i
        maxlenvalue = listt[i]

print("Max length:", maxlen)
print("Index:", maxlenindex)
print("Value:", maxlenvalue)
