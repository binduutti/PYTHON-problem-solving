'''
Find the first occurrence of a target value in an array.
'''
arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))

first_occ = -1   

for i in range(len(arr)):
    if arr[i] == target:
        first_occ = i
        break

print("First occurrence:", first_occ)
