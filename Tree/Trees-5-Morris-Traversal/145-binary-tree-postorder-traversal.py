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




def reverse_path(start, end):
    prev = None
    current = start
    while prev != end:
        nxt = current.right
        current.right = prev
        prev = current
        current = nxt
        
def collect_reverse(from_node, to_node, result):
    reverse_path(from_node, to_node)

    node = to_node
    while True:
        result.append(node.val)
        if node == from_node:
            break
        node = node.right

    reverse_path(to_node, from_node)



class Solution:
    
    def postorder_morris_traversal_simple(self, root : BinaryTreeNode):
        
        result = []
        
        current_ptr = root
        
        while current_ptr:
            if not current_ptr.right: ## Change left to right
                result.append(current_ptr.val)
                current_ptr = current_ptr.left #change right to left
            else:                
                predecessor_ptr =  current_ptr.right ## Change left to right
                while predecessor_ptr.left and predecessor_ptr.left != current_ptr:  #change right to left
                    predecessor_ptr = predecessor_ptr.left  #change right to left
                    
                if not predecessor_ptr.left:  #change right to left
                    result.append(current_ptr.val)
                    predecessor_ptr.left = current_ptr  #change right to left
                    current_ptr = current_ptr.right ## Change left to right
                else:
                    predecessor_ptr.left = None  #change right to left
                    current_ptr = current_ptr.left  #change right to left
        
        return result[::-1]
        
        
        
        
        
        
        
        
    
    def postorder_morris_traversal_complex(self, root: BinaryTreeNode):
        
        result = []
        dummy = BinaryTreeNode(0)
        dummy.left = root
        current_ptr = dummy
        
        while current_ptr:
            if not current_ptr.left: ## This is where you are backtracking to previous node via the ephemeral path you created earlier
                current_ptr = current_ptr.right 
            else:
                predecessor_ptr = current_ptr.left ## Move your predecessor pointer  all teh to the right dead end
                while predecessor_ptr.right and predecessor_ptr.right != current_ptr:
                    predecessor_ptr = predecessor_ptr.right
            
                if not predecessor_ptr.right:   ## This is where you create an ephemeral path from right dead end node to current                 
                    predecessor_ptr.right = current_ptr
                    current_ptr = current_ptr.left  ##and advance the current pointer to the left
                else:                   
                    collect_reverse(current_ptr.left, predecessor_ptr, result)
                    predecessor_ptr.right = None  ## You break the path you created earlier.
                    current_ptr = current_ptr.right ## and reach teh current pointer to right

        return result      





if __name__ == "__main__":
    values = [3,9,20,None,None,15,7]
    
    
    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    print(f'Complex Solution : {sol.postorder_morris_traversal_complex(root)}')
    print(f'Simple Solution : {sol.postorder_morris_traversal_simple(root)}')
