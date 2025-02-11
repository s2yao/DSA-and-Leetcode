# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root): # This is DFS
        res = []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):
                res.append(node.val)  # First node at this depth (rightmost)
            dfs(node.right, depth + 1)  # Visit right first
            dfs(node.left, depth + 1)   # Then left
        
        dfs(root, 0)
        return res
    


    def rightSideView2(self, root): # This is BFS
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:  # Last node of this level
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res


