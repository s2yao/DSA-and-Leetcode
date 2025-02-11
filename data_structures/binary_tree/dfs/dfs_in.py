class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# In order
def in_order(curr_node):
    if not curr_node: return

    in_order(curr_node.left)
    print(curr_node.val)
    in_order(curr_node.right)

def in_order_iterative(curr_node):
    if not curr_node: return

    stack = []
    curr = curr_node

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        print(curr.val)
        curr = curr.right