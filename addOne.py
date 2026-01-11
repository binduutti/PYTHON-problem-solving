''' write a python function to add one to a number represented as an array of digits.
For example, if the input array is [1, 2, 3], the output should be [1, 2, 4].'''

li = list(map(int, input().split()))

for i in range(len(li) - 1, -1, -1):
    if li[i] != 9:
        li[i] += 1
        break
    else:
        li[i] = 0
else:
    li = [1] + li

print(li)
