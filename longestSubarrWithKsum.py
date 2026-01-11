''' given an array of integers nums and an integer value k , return the length of the longest subarray that sums to k.
example:
Input: nums = [1, -1, 5, -2, 3],
k = 3
Output: 4'''
def longest_subarray_with_k_sum(nums, k):
    sum_index_map = {}
    current_sum = 0
    max_length = 0

    for i in range(len(nums)):
        current_sum += nums[i]

        if current_sum == k:
            max_length = i + 1

        if (current_sum - k) in sum_index_map:
            max_length = max(max_length, i - sum_index_map[current_sum - k])

        if current_sum not in sum_index_map:
            sum_index_map[current_sum] = i

    return max_length