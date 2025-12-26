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
    
    def count_univalue_subtree_optimal_too_complex_and_redundant(self, root: BinaryTreeNode):
        global_univalue_count = 0

        
        def helper(node : BinaryTreeNode):   
            nonlocal global_univalue_count
            
            
            unival_left = None
            unival_right = None
            
            if not node:
                return
        
            
            if node.left:
                unival_left = helper(node.left)
            if node.right:                
                unival_right = helper(node.right)
            
            
            if not node.left and not node.right:
                global_univalue_count += 1
                return True
            
            if  (node.left and node.right) and (unival_left and unival_right):
                print(f'{node.val} --- {node.left.val} {node.right.val}')
                if (node.val == node.left.val) and (node.val == node.right.val):
                    global_univalue_count += 1
                    return True
                else:
                    return False
            elif (node.left and not node.right) and (unival_left):
                if (node.val == node.left.val):
                    global_univalue_count += 1
                    return True
            elif (node.right and not node.left) and (unival_right):
                if (node.val == node.right.val):
                    global_univalue_count += 1
                    return True
            else:            
                return False
                
        
        helper(root)
        return global_univalue_count
    
    
    
    def count_univalue_subtree_optimal(self, root: BinaryTreeNode):
        global_univalue_count = 0

        
        def helper(node : BinaryTreeNode):   
            nonlocal global_univalue_count
            
            if not node:
                return True
        
            
            unival_left = helper(node.left)
            unival_right = helper(node.right)
            
            if not unival_left or not unival_right:
                return False
            
            if node.left and (node.val != node.left.val):
                return False
                
            if node.right and (node.val != node.right.val):
                return False
            
            global_univalue_count += 1
            return True
            
        helper(root)
        return global_univalue_count       

if __name__ == "__main__":
    values = []
    #values = [5,1,5,5,5,None,5]
    # values = [5,5,5,5,5,None,5]
    values = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,5,6,5,6,7]
    

    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
#    print(f'univalue count : {sol.count_univalue_subtree_optimal_too_complex_and_redundant(root)}')
    print(f'univalue count : {sol.count_univalue_subtree_optimal(root)}')
