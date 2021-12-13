class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right, self.left = None, None


def find_diameter(root):
    diameter = 0

    def calculate_diameter(current_node):
        nonlocal diameter
        if current_node is None:
            return 0

        left_height = calculate_diameter(current_node.left)
        right_height = calculate_diameter(current_node.right)
        current_diameter = left_height + right_height + 1
        diameter = max(current_diameter, diameter)
        return max(left_height, right_height) + 1
    return calculate_diameter(root)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
print(find_diameter(root))
