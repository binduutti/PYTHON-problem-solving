'''
Write a Python program to count the frequency of each element in a list and store the result as a list of lists, where each sublist contains an element and its corresponding frequency.
Example:
Input: [1, 2, 2, 3, 3, 3]
Output: [[1, 1], [2, 2], [3, 3]]

'''
listt = list(map(int, input("Enter Numbers: ").split()))
d = {}
res = []

for i in listt:
    d[i] = d.get(i, 0) + 1

for k, v in d.items():
    res.append([k, v])

print(res)
