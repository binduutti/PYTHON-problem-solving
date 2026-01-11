''' given an array of integers nums and return the maximum value in the array using exception handling to manage potential errors. '''


def find_maximum(arr):
    try:
        if not arr:
            raise ValueError("The array is empty.")
        maximum = arr[0]
        for num in arr:
            if not isinstance(num, int):
                raise TypeError("All elements must be integers.")
            if num > maximum:
                maximum = num
        return maximum
    except ValueError as ve:
        return str(ve)
    except TypeError as te:
        return str(te)
li = list(map(int, input().split()))
print(find_maximum(li))