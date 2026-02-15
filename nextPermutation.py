'''
given an array of integers nums, find the next permutation of nums.
The next permutation of an array of integers is the next lexicographically greater permutation of its integers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.
example:
Input: nums = [1,2,3]
Output: [1,3,2]
'''
def next_permutation(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i == -1:
        nums.reverse()
        return
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])
nums = [1, 2, 3]
next_permutation(nums)
print("Next permutation is:", nums)