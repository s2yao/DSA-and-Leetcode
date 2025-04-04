def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right: # the last comparison
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    
    return -1

# the binary search the find the threshhold of the smallest element

def binary_search(arr, target):
    left = 0
    right = len(arr)

    while left < right: # the last comparison
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return right if right < len(arr) else -1