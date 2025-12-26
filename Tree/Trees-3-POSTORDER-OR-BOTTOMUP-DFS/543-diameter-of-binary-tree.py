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

    def diameter_of_binary_tree(self, root: BinaryTreeNode):
        
        global_max = float("-inf")
        
        
        def helper(node: BinaryTreeNode):
            nonlocal global_max
            
            if not node:
                return 0
            
            # Tree traversing
            my_right_subtree_height = helper(node.right)            
            my_left_subtree_height = helper(node.left)            
            
            #Actual work    
            # max diameter computation        
            global_max = max(global_max, my_right_subtree_height + my_left_subtree_height)
            
            #need to return my height
            my_height = max(my_right_subtree_height, my_left_subtree_height) + 1                        
            return my_height

    
        helper(root)
        
        return global_max


if __name__ == "__main__":
    values = [1,2,3,4,5]

    #values = [1,2]
    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    print(sol.diameter_of_binary_tree(root))
