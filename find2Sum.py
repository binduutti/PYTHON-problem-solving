''' Find two numbers in an array that sum up to a specific target. 
e.g., if the input array is [2, 7, 11, 15] and the target is 9, the output should be (0, 1) because numbers[0] + numbers[1]'''
def two_sum(nums, target):
    seen = {}  

    for i in range(len(nums)):
        needed = target - nums[i]

        if needed in seen:
            return (seen[needed], i)

        seen[nums[i]] = i
    return None
li=list(map(int,input().split()))
t=int(input())
result=two_sum(li,t)
print(result)