class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
def bfs(root):
    if not root: return
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)


# if want to iterate each level from top to bottom
def bfs(root):
    if not root: return
    queue = deque([root])
    curr_max, curr_sum = root.val, 0
    
    while queue:
        curr_len = len(queue)
        for i in range(curr_len):
            node = queue.popleft()
            # Action, say i want the maximum level
            curr_sum += node.val
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        curr_max = max(curr_max, curr_sum)
        curr_sum = 0
    
    return curr_max