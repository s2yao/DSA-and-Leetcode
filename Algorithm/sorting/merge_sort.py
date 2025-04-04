def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merging(left, right)

def merging(left, right):
    i = 0
    j = 0
    ret = []
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ret.append(left[i])
            i += 1
        else:
            ret.append(right[j])
            j += 1
    
    ret.extend(left[i:])
    ret.extend(right[j:])

    return ret