'''
We added a new parameter for condition checking
Multiple condition checks can occur in form of if elif
'''
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        # k is the max len of valid comb
        # n is the target sum

        ret = []

        def backtrack(index, path, curr_sum):
            if curr_sum == n and len(path) == k:
                # if curr_sum is valid and length is valid
                ret.append(list(path))
                return

            elif len(path) >= k or curr_sum > n:
                return
            
            for num in range(index, 10):
                path.append(num)
                backtrack(num + 1, path, curr_sum + num) # If we want all combinations no matter what
                path.pop()
         
        backtrack(1, [], 0)
        return ret
    
    sol = Solution()
    print(sol.combinationSum3(3, 7))