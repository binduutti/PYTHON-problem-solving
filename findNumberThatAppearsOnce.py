# Python implementation to find the number that appears only once in an array

nums=[4,1,2,1,2]
xor=0
for num in nums:
    xor ^= num
print("The number that appears only once is:", xor)
