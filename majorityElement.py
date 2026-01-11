'''Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times. You may assume that the array is non-empty and the majority element always exists in the array.
e.g., if the input array is [3,2,3], the output should be 3 because 3 appears twice which is more than ⌊3/2⌋ = 1 time.'''
def majority_element(nums):
    n = len(nums) // 2
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for key, value in freq.items():
        if value > n:
            return key

    return -1
    
nums = list(map(int, input().split()))
majele=majority_element(nums)
print(majele)