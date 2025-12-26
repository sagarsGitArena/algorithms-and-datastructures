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
    
    
    def min_dist_between_bst_nodes(self, root: BinaryTreeNode):
        prev = None
        global_min = float("Inf")
        def helper(node : BinaryTreeNode):
            nonlocal prev, global_min
            
            if not node:
                return       
            
            helper(node.left)
            
            if prev:
                diff = node.val - prev.val
                global_min = min (diff, global_min)
            
            prev = node
            helper(node.right)

    
        helper(root)     
        return  global_min



if __name__ == "__main__":
    values = [4,2,6,1,3]
    
    
    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    print(f'Optimal : {sol.min_dist_between_bst_nodes(root)}')
