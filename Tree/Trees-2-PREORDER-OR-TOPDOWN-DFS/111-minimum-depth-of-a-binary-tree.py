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
# largest value in each tree row
    def minimum_depth_of_a_binary_tree( self, root : BinaryTreeNode):
        
        if root is None:
            return 0
        
        min_depth = float("inf")        
        
        def helper(node :BinaryTreeNode, level: int):
            nonlocal min_depth
    
            level+=1
    
            if node.left is None and node.right is None:
                min_depth = min(min_depth, level)
                return
            
            if node.left:
                helper(node.left, level)
                
            
            if node.right:
                helper(node.right, level)
                
        helper(root, 0)

        return min_depth                  
        

        
        


if __name__ == "__main__":
    values = [3,9, 20,None, None, 15, 7]
    values = [2, None, 3, None, 4, None, 5, None, 6]
    
    

    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    results = sol.minimum_depth_of_a_binary_tree(root)
    print(results)
    