# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ret = [0]
        def traversal(root, curr_max):
            if not root: 
                return
            if root.val >= curr_max:
                curr_max = root.val
                ret[0] += 1
            traversal(root.left, curr_max)
            traversal(root.right, curr_max)
        
        traversal(root, root.val)
        return ret[0]