'''
write a function that takes in an array of integers and returns a dictionary with the frequency of each integer in the array.
Example:
Input: [1, 2, 2, 3, 3, 3]
Output: {1: 1, 2: 2, 3: 3}
'''

def count_frequencies(arr):
    frequency_dict = {}
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    return frequency_dict   
# Example usage:
input_array = [1, 2, 2, 3, 3, 3]
result = count_frequencies(input_array)
print(result)