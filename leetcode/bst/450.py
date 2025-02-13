# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# What a pain in the fucking ass

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None  # If tree is empty, return None

        # Recursive lookup & deletion
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Case 1: No left child
            if not root.left:
                return root.right
            # Case 2: No right child
            elif not root.right:
                return root.left
            # Case 3: Two children → Find the inorder successor (smallest in right subtree)
            else:
                successor = self.getMin(root.right)  # Get the min node in right subtree
                root.val = successor.val  # Replace root value with successor value
                root.right = self.deleteNode(root.right, successor.val)  # Delete successor node

        return root  # Return the modified tree

    # Helper function to find the minimum node in a subtree
    def getMin(self, node):
        while node.left:
            node = node.left
        return node
