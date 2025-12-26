# edges along the path
# vertices along the path

# from typing import Optional, List
from collections import deque


# --------------------------
# TreeNode definition
# --------------------------

class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left=left
        self.right=right



# --------------------------
# Print tree sideways
# --------------------------
def print_tree(node: BinaryTreeNode | None, prefix: str = "", is_left: bool = True):
    if node is None:
        return

    # Print right child first
    if node.right:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)

    # Print current node
    print(prefix + ("└── " if is_left else "┌── ") + str(node.val))

    # Print left child
    if node.left:
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)



def build_tree(values : list[int | None]) -> BinaryTreeNode | None:
    if not values:
        return None
    
    root = BinaryTreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if values[i] is not None:
            node.left = BinaryTreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i >= len(values):
            break
        
        if values[i] is not None:
            node.right = BinaryTreeNode(values[i])
            queue.append(node.right)
        i += 1
        
    return root

class Solution:
    
    
    def binary_tree_maximum_path_sum(self, root: BinaryTreeNode):
        
        global_max_path_sum = 0
        
        def helper(node : BinaryTreeNode):
            nonlocal global_max_path_sum
            
            if not node:
                return 0
            
            
            left_tree_sum = helper(node.left)
            
            right_tree_sum = helper(node.right)
            
            node_sum = left_tree_sum + right_tree_sum + node.val
            
            global_max_path_sum = max(node_sum, global_max_path_sum)
            
            local_max =  max(left_tree_sum, right_tree_sum) + node.val
            
            return local_max
            
        helper(root)
        return global_max_path_sum



if __name__ == "__main__":
    values = [1,2,3]
    values = [-10,9,20,None, None, 15,7]
    values = [1,2,3,4,5]
    
    
    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    print(f'Optimal : {sol.binary_tree_maximum_path_sum(root)}')
