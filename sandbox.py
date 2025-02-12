from collections import deque
# bfs for tree
# print all node in dfs ordering
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# BFS for Tree
def bfs_tree(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

# Preorder Recursive
def pre_dfs_tree(root):
    if not root: return
    print(root.val)
    pre_dfs_tree(root.left)
    pre_dfs_tree(root.right)

# Preorder Iterative
def pre_dfs_iterative_tree(root):
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)

# Inorder Recursive
def in_dfs_tree(root):
    if not root: return
    in_dfs_tree(root.left)
    print(root.val)
    in_dfs_tree(root.right)

# Inorder Iterative
def in_dfs_iterative_tree(root):
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.val)
        curr = curr.right

# Postorder Recursive
def post_dfs_tree(root):
    if not root: return
    post_dfs_tree(root.left)
    post_dfs_tree(root.right)
    print(root.val)

# Postorder Iterative
def post_order_iterative(root):
    if not root: return
    
    stack = []
    result = []
    last_visited = None
    curr = root

    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left  # Keep going left
        else:
            peek = stack[-1]  # Look at the top node without popping
            if peek.right and last_visited != peek.right:
                curr = peek.right  # Process right subtree if not visited
            else:
                result.append(peek.val)  # Add to result (postorder)
                last_visited = stack.pop()  # Mark as visited

    print(result)  # No need for reversing!

