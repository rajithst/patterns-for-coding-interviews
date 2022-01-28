class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def count_path_for_given_sum(root,given_sum):
    dfs_traversal(root,given_sum,[])


def dfs_traversal(current_node,given_sum,current_path):
    if current_node is None:
        return 0

    current_path.append(current_node.val)
    path_count,path_sum = 0,0

    for i in range(len(current_path)-1,-1,-1):
        path_count+=current_path[i]
        if path_sum == given_sum:
            path_count+=1

    dfs_traversal(current_node.left,given_sum,current_path)
    dfs_traversal(current_node.right)



