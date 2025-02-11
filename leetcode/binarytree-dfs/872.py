# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        arr1 = []
        arr2 = []

        def traversal(root, arr):
            if not root: return
            if not root.left and not root.right:
                arr.append(root.val)
            
            traversal(root.left, arr)
            traversal(root.right, arr)

        traversal(root1, arr1)
        traversal(root2, arr2)
        
        return arr1 == arr2
