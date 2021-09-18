class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right, self.left = None, None


class Solution:
    def __init__(self):
        self.diameter = 0

    def find_diameter(self, root):
        self.calculate_diameter(root)
        return self.diameter

    def calculate_diameter(self, current_node):
        if current_node is None:
            return 0

        left_height = self.calculate_diameter(current_node.left)
        right_height = self.calculate_diameter(current_node.right)

        if current_node.left is not None and current_node.right is not None:
            current_diameter = left_height + right_height + 1
            self.diameter = max(current_diameter, self.diameter)

        return max(left_height, right_height) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
solution = Solution()

print("Tree Diameter: " + str(solution.find_diameter(root)))
