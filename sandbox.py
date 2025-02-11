def maxBarrier(n, initialEnergy, th):
    initialEnergy.sort()  # Sort in ascending order
    low = initialEnergy[0]
    high = initialEnergy[-1]  # The largest element in the sorted list
    
    while low < high:
        mid = (low + high + 1) // 2
        if sum(max(energy - mid, 0) for energy in initialEnergy) >= th:
            low = mid  # Increase the barrier (move low up)
        else:
            high = mid - 1  # Lower the barrier (move high down)
    
    return low  # Return the maximum barrier

# Test the function
initialEnergy = [3, 9, 7, 6]
print(maxBarrier(4, initialEnergy, 6))  # Expected output based on problem conditions
