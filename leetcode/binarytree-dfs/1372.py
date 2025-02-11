# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        self.ret = 0

        def traversal(root, left, right):
            self.ret = max(self.ret, left, right)

            if root.left:  # If we can go left
                traversal(root.left, right + 1, 0)
            if root.right:  # If we can go right
                traversal(root.right, 0, left + 1)

        traversal(root, 0, 0)
        return self.ret
    

    def longestZigZag2(self, root):
        self.ret = 0

        def traversal(root, length, direction):
            if not root: return
            self.ret = max(self.ret, length)

            if direction == "left":
                traversal(root.right, length + 1, "right")
                traversal(root.left, 1, "left")

            if direction == "right":
                traversal(root.left, length + 1, "left")
                traversal(root.right, 1, "right")

        traversal(root.left, 1, "left")
        traversal(root.right, 1, "right")

        return self.ret

        
            


        