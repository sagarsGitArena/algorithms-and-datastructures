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
    
    
    def morris_preorder_traversal(self, root: BinaryTreeNode):
        result = []
        current_ptr = root
        predecessor_ptr = None
        
        while current_ptr:
            if not current_ptr.left:
                result.append(current_ptr.val)
                current_ptr = current_ptr.right                
            else:
                predecessor_ptr = current_ptr.left 
                
                while predecessor_ptr.right and predecessor_ptr.right != current_ptr:
                    predecessor_ptr = predecessor_ptr.right
                    
                if not predecessor_ptr.right:
                    result.append(current_ptr.val)
                    predecessor_ptr.right = current_ptr
                    current_ptr = current_ptr.left
                else:                 
                    predecessor_ptr.right = None                    
                    current_ptr = current_ptr.right
        
        
        return result



if __name__ == "__main__":
    values = [3,9,20,None,None,15,7]
    
    
    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    print(f'Optimal : {sol.morris_preorder_traversal(root)}')
