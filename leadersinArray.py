'''
given an array of integers, find all the leaders in the array.
An element is called a leader if it is greater than all the elements to its right side.
For example, in the array [16, 17, 4, 3, 5, 2], the leaders are 17, 5, and 2.
Example:
Input: [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
'''
li = [-3, 4, 5, 1, -4, -5]
n = len(li)
leaders = []
for i in range(n):
    isLeader = True
    for j in range(i+1, n):
        if li[i] < li[j]:
            isLeader = False
            break
    if isLeader:
        leaders.append(li[i])
print(leaders)