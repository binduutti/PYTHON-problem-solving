'''
write a program to reverse a list using recursion.
example:
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

'''

def rev(arr):
    if not arr:
        return []
    
    x = arr.pop()
    print(x, end=" ")   
    return [x] + rev(arr)

listt = list(map(int, input("Enter list: ").split()))
result = rev(listt.copy())

print("\nAs list:", result)