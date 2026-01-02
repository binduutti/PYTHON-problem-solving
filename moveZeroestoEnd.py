'''
Move all the zeros in a list to the end while maintaining the order of non-zero elements.
'''
listt = list(map(int, input().split()))
n = len(listt)

index = 0

for i in range(n):
    if listt[i] != 0:
        listt[index] = listt[i]
        index += 1

for i in range(index, n):
    listt[i] = 0

print(listt)
