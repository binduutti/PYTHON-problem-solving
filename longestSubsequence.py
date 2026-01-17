'''Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity 
example 1:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
'''

nums = list(map(int,input().split()))
n = len(nums)
count = 1
longSeq = 1
nums.sort()

if(len(nums)==0):
    print(0)
    exit()
ptr = nums[0]
for i in range(1,len(nums)):
    if nums[i]==ptr:
        continue
    elif nums[i]==(ptr+1):
        count = count+1
        ptr = nums[i]
        longSeq=max(longSeq,count)
    else:
        ptr = nums[i]
        count =1

print(longSeq)