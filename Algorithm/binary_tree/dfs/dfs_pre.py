class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Pre order
def pre_order(curr_node):
    if not curr_node: return
    print(curr_node.val)
    pre_order(curr_node.left)
    pre_order(curr_node.right)

def pre_order_iterative(curr_node):
    if not curr_node: return

    stack = [curr_node]

    while stack:
        node = stack.pop()
        print(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)