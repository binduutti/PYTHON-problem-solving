def merge_sort(arr, l, u):
    if l >= u:
        return
    
    mid = (l + u) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, u)
    merge(arr, l, mid, u)

def merge(arr, l, mid, u):
    mergelist = []
    i = l
    j = mid + 1

    while i <= mid and j <= u:
        if arr[i] < arr[j]:
            mergelist.append(arr[i])
            i += 1
        else:
            mergelist.append(arr[j])
            j += 1

    while i <= mid:
        mergelist.append(arr[i])
        i += 1

    while j <= u:
        mergelist.append(arr[j])
        j += 1

    # Copy back to original array
    for idx in range(len(mergelist)):
        arr[l + idx] = mergelist[idx]

n = int(input())
arr = []
while len(arr) < n:
    arr.extend(map(int, input().split()))
arr = arr[:n]

merge_sort(arr, 0, len(arr)-1)
print(arr)
