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
    
    
    def inorder_morris_traversal(self, root: BinaryTreeNode):
        is_valid_bst = True        
        prior_node_val = float("-inf")
        
        current_ptr = root
        while current_ptr:
            if not current_ptr.left: ## This is where you are backtracking to previous node via the ephemeral path you created earlier
                
                ###### ACTUAL WORK ###########
                if current_ptr.val <= prior_node_val:
                    is_valid_bst = False
                prior_node_val = current_ptr.val
                ##############################
                current_ptr = current_ptr.right 
            else:
                predecessor_ptr = current_ptr.left ## Move your predecessor pointer  all teh to the right dead end
                while predecessor_ptr.right and predecessor_ptr.right != current_ptr:
                    predecessor_ptr = predecessor_ptr.right
            
                if not predecessor_ptr.right:   ## This is where you create an ephemeral path from right dead end node to current                 
                    predecessor_ptr.right = current_ptr
                    current_ptr = current_ptr.left  ##and advance the current pointer to the left
                else:                   
                    predecessor_ptr.right = None  ## You break the path you created earlier.
                ###### ACTUAL WORK ###########
                if current_ptr.val <= prior_node_val:
                    is_valid_bst = False
                prior_node_val = current_ptr.val
                ##############################
                current_ptr = current_ptr.right ## and reach teh current pointer to right
          
        return is_valid_bst
    
    
    #def inorder_morris_traversal_selftest(self, root: BinaryTreeNode):
        
        



if __name__ == "__main__":
    values = [3,9,20,None,None,15,7]
    
    values = [6,4,9,3,5,7,None,None,None,None,None,None,8]
    
    
    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    print(f'Optimal : {sol.inorder_morris_traversal(root)}')
