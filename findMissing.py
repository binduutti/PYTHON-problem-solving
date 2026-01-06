'''Python program to find the missing number in a list of numbers from 0 to n'''

nums=[0,1,2]
n=len(nums)
miss=(n*(n+1))//2
for i in range(n):
    miss-=nums[i]
print("Missing:",miss)