# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth_post(self, root):
        if not root: return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth) # This is post ordering


    def maxDepth_pre(self, root):
        if not root: return 0
        ret = [1]

        def traversal(root, depth):
            if not root: return

            ret[0] = max(ret[0], depth)
            traversal(root.left, depth + 1)
            traversal(root.right, depth + 1)

        traversal(root, 1)
        return ret