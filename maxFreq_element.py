'''
write a Python program to find the element with the highest frequency in a list.
example:
Input: [1, 2, 2, 3, 3, 3]
Output: 3

'''
listt = list(map(int, input("Enter numbers: ").split()))
d = {}
res = []

for i in listt:
    d[i] = d.get(i, 0) + 1

maxkey=0
maxvalue=0
for key in d:
    if d.get(key)>maxvalue:
        maxvalue=d.get(key)
        maxkey = key


print(maxkey)
