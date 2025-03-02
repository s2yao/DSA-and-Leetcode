'''
The key is to realize that if we negative every element

We have created max_heap, using min_heap
'''
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)
        ret = 0

        for _ in range(k): # O(n)
            ret = -heapq.heappop(max_heap)

        return ret

'''
Count sort algo
'''

def findKthLargest2(nums, k):
    max_ele = max(nums)
    min_ele = min(nums)

    arr = [0] * max_ele - min_ele
    
    for value in nums:
        arr[value - min_ele] += 1
    
    remain = k
    for i in reversed(range(len(arr))):
        remain -= arr[i]
        if remain <= 0:
            return i + min_ele
    
    return -1

