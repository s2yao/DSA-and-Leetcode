# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1 # Since path can start from root
        self.ret = 0

        def traversal(root, length):
            if not root: return
            
            length += root.val
            self.ret += prefix_sum[length - targetSum]

            prefix_sum[length] += 1
            traversal(root.left, length)
            traversal(root.right, length)
            prefix_sum[length] -= 1
        
        traversal(root, 0)
        return self.ret
        

