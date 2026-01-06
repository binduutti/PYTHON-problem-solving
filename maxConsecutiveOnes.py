# Find the maximum number of consecutive 1's in an array of binary numbers.
nums=[1,1,1,1,0,1,1,1]
n=len(nums)
max_ones=0
count=0
for i in range(n):
    if nums[i]==1:
        count+=1

    else:
        count=0
    max_ones=max(max_ones,count)
print("Max consecutive 1's:",max_ones)
