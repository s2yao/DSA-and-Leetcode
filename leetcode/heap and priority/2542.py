'''
Fucking genius

If we want the maximum value for any operations on 2 list, where these 2 list is pair to pair basis

We can always zip it first, and sort one of the zipped obj first

And to iterate the other zipped obj for explore other possible maximums
'''
class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        nums_zip = zip(nums1, nums2)

        pairs_sorted = sorted(nums_zip, key = lambda x: -x[1]) # Sorting based on the second element of this zipped iterable

        curr_k = [x for x, y in pairs_sorted[:k]]

        heapify(curr_k)

        curr_sum = sum(curr_k)

        curr_ret = curr_sum * pairs_sorted[k - 1][1] # The current ret value
        # Note that anywhere lower than pairs_sorted[k - 1][1] is be smaller than itself

        for x, y in pairs_sorted[k:]:
            # And we only need to consider x, since y is decreasing
            if x > curr_k[0]:
                curr_sum += x - heapreplace(curr_k, x)
                curr_ret = max(curr_ret, curr_sum * y)
        
        return curr_ret