'''
The key is to realize that 
1. When we need to get an element out of an array, at the same time have a quick look up for the popped element's original position
2. When the original array is reordered into multiple parts, we can combine all the parts into one heap, and to keep tract of adding new elements / deleting old elemenets
'''

class Solution(object):
    def totalCost(self, costs, k, candidates):
        # We first zip together costs and its index
        # index is on 1st position
        cost_index = zip(costs, range(len(cost)))

        # We define a left and right index on the original cost_index
        # Since we will heap both side of the costs into one heap list
        left = candidates - 1 # the posn that the last element of left candidates
        right = len(cost_index) - candidates # the posn that the last element of right candidates

        heap = []
        # Now we chech any overlaping workers
        if len(costs) >= candidates * 2:
            heap = cost_index[:candidates] + cost_index[-candidates:]
        else:
            heap = cost_index
        heapify(heap)
        # Now we have the heap at which we will be taking out elements
        ret_cost = 0
        for _ in range(k):
            # Check for potential duplicates using left and right
            if left + 1 < right: # To ensure that there is at least 1 worker between left and right
                curr_min = heappop(heap)
                ret_cost += curr_min
                if curr_min[1] <= left: # if the current element is in left window
                    left += 1
                    heappush(heap, cost_index[left])
                else:
                    right -= 1
                    heappush(heap, cost_index[right])

            else: # overlap occurs, no need for updating
                ret_cost += heappop(heap)[0]

        return ret_cost