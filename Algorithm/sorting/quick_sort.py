def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    
    left = []
    right = []
    mid = []

    for element in arr:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            mid.append(element)
    
    return quick_sort(left) + mid + quick_sort(right)