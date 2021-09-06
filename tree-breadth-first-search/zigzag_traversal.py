from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


#sigzag traversal,starting from left to right
#since this is level by level- use BFS
#if moving direction is left to right,append level values to right
#if moving direction is right to left, append level values to left
# since level values are append to left and right,use deque to level value queue
# after end of each level change the moving direction
def zigzag_traversal(root):
    que = deque()
    que.append(root)
    left_to_right = True
    results = []
    while que:

        level_length = len(que)
        level_results = deque()
        for _ in range(level_length):
            current_node = que.popleft()
            if left_to_right:
                level_results.append(current_node.val)
            else:
                level_results.appendleft(current_node.val)

            if current_node.left:
                que.append(current_node.left)
            if current_node.right:
                que.append(current_node.right)
        results.append(level_results)
        left_to_right = not left_to_right
    return results


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(20)
root.right.left.right = TreeNode(17)
print("Zigzag traversal: " + str(zigzag_traversal(root)))
