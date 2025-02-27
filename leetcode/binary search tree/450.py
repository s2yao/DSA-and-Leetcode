# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# What a pain in the fucking ass

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None

        if root.val == key:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                replacement_node = root.right
                while replacement_node.left:
                    replacement_node = replacement_node.left
                root.val = replacement_node.val
                root.right = self.deleteNode(root.right, replacement_node.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root