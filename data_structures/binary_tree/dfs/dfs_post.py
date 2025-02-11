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
def post_order_iterative(curr_node):
    if not curr_node: return

    stack1 = [curr_node]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left: stack1.append(node.left)
        if node.right: stack1.append(node.right)

    while stack2:
        print(stack2.pop().val)