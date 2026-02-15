'''Kadanes Algorithm to find the maximum sum subarray along with the subarray itself.
Input: An array of integers.
Output: The maximum sum of the contiguous subarray and the subarray itself.
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output:  The contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''

li=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
def kadanes_algorithm(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    start = 0
    end = 0
    temp_start = 0
    for i in range(1, len(arr)):
        if current_sum + arr[i] > arr[i]:
            current_sum += arr[i]
        else:
            current_sum = arr[i]
            temp_start = i
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    return max_sum, arr[start:end+1]
result_sum, result_subarr = kadanes_algorithm(li)
print("Maximum sum is:", result_sum)
print("Subarray is:", result_subarr)
