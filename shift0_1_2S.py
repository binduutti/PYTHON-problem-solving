''' Given an array nums with n objects colored red, white, or blue,
  the goal is to sort the array in-place so that objects of the same color are adjacent,
  with the red objects (0) on the left, white objects (1) in the middle, and blue objects (2) on the right.
 '''
li = list(map(int, input().split()))
n = len(li)
zerocount = 0
onecount = 0
twocount = 0
for i in range(n):
    if li[i] == 0:
        zerocount += 1
    elif li[i] == 1:
        onecount += 1
    else:
        twocount += 1
index = 0
for i in range(zerocount):
    li[index] = 0
    index += 1
for i in range(onecount):
    li[index] = 1
    index += 1
for i in range(twocount):
    li[index] = 2
    index += 1

print(li)
