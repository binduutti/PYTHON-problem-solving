''' Rotate an array by one place to the left '''
nums=[1,2,3,4,5]
n=len(nums)
temp=nums[0]
for i in range(n-1):
    nums[i]=nums[i+1]
nums[n-1]=temp
print("Array after rotation:",nums)
