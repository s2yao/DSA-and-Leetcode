# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ret = 1
        curr_sum = 0
        curr_max = root.val
        depth = 0

        while queue:
            curr_len = len(queue)
            curr_sum = 0
            depth += 1
            for i in range(curr_len):
                node = queue.popleft()
                curr_sum += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if curr_sum > curr_max:
                ret = depth
                curr_max = curr_sum
        return ret

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sumAtDepth = defaultdict(int)

        # DFS function to calculate sum at each depth
        def dfs(node, depth):
            if not node:
                return
            
            # Add current node's value to its depth's sum
            sumAtDepth[depth] += node.val

            # Recur for left and right children
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        # Start DFS from root at depth 1
        dfs(root, 1)

        # Return the level with the maximum sum
        return max(sumAtDepth, key=sumAtDepth.get)