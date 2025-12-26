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
    
    def longest_univalue_path(self, root: BinaryTreeNode):
        global_longest_univalue_path = 0
       
        
        def helper(node: BinaryTreeNode):
            nonlocal global_longest_univalue_path            
            
            if not node:
                return 0
            
            print(f'{node.val}')
            left_length = helper(node.left)
            
            right_length = helper(node.right)
            
            ## Work
            if node.left and (node.left.val == node.val):
                left_length  += 1
            
            if node.right and (node.right.val == node.val):
                right_length  += 1
                

                
            global_longest_univalue_path = max(global_longest_univalue_path, right_length + left_length)     
            return max(right_length, left_length)                   
            
        helper(root)
        return global_longest_univalue_path
                
            
            



if __name__ == "__main__":
    values = [5,4,5,1,1,None,5]
    values = [1,4,5,4,4,None,5]

    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    print(f'Optimal : {sol.longest_univalue_path(root)}')
    