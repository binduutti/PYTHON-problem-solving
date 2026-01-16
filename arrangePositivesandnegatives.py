'''
Given a 0-indexed integer array nums of even length n consisting of equal
numbers of positive and negative integers. 
example: [3,1,-2,-5,2,-4]
Rearrange the elements of nums such that the modified array follows the
following conditions:
1. Every consecutive pair of integers have opposite signs.
2. For all integers with the same sign, the order in which they were present
    in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the conditions.
output: [3,-2,1,-5,2,-4]
'''


list_nums = [3, 1, -2, -5, 2, -4]

def rearrange_array(nums):
    n = len(nums)
    temp = [0] * n
    evenindex = 0
    oddindex = 1
    for i in range(n):
        if nums[i] > 0:
            temp[evenindex] = nums[i]
            evenindex += 2
        else:
            temp[oddindex] = nums[i]
            oddindex += 2
    return temp
result = rearrange_array(list_nums)