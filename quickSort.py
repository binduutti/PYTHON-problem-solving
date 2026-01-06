'''Python implementation of QuickSort algorithm'''
def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def partition(arr, lb, ub):
    pivot = arr[lb]
    start = lb
    end = ub

    while start < end:
        while start < ub and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            swap(arr, start, end)

    swap(arr, lb, end)
    return end

def quicksort(arr, lb, ub):
    if lb < ub:
        loc = partition(arr, lb, ub)
        quicksort(arr, lb, loc - 1)
        quicksort(arr, loc + 1, ub)

listt = list(map(int, input().split()))
n = len(listt)

quicksort(listt, 0, n - 1)
print(listt)
