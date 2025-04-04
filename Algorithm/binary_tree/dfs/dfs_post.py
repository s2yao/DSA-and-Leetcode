class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Post order
def post_order(curr_node):
    if not curr_node: return

    post_order(curr_node.left)
    post_order(curr_node.right)
    print(curr_node.val)

# Recursive implementations
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
