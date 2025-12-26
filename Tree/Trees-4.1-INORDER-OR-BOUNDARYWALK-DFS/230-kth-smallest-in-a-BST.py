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
    
    
    def kth_smallest_in_bst(self, root: BinaryTreeNode, k: int):
        kth_smallest = None
        global_index = 0
        global_k = k
        
        def helper(node : BinaryTreeNode):
            nonlocal kth_smallest
            nonlocal global_index
            nonlocal global_k
            
            if kth_smallest:
                return
            
            if not node:
                return
            
            if node.left:
                helper(node.left)
            
            print(node.val)
            
            global_index += 1
            if global_index == global_k:
                kth_smallest = node.val
            
            
            if node.right:
                helper(node.right)
            
            
    
        helper(root)  
        return kth_smallest    

    def kth_smallest_in_bst_better(self, root: BinaryTreeNode, k: int):
        global_kth_smallest = None
        
        def helper(node : BinaryTreeNode):
            
            nonlocal global_kth_smallest
            nonlocal k
            
            
            
            if not node or global_kth_smallest:
                return
            
            helper(node.left)
            
            print(node.val)
            
            k -= 1
            if k == 0:
                global_kth_smallest = node.val
                return
            
            helper(node.right)
            
            
    
        helper(root)  
        return global_kth_smallest    



if __name__ == "__main__":
    values = [3,1,4,None,2]
    values = [5,3,6,2,4,None,None,1]
    
    
    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    print(f'Good : {sol.kth_smallest_in_bst(root, 2)}')
    print(f'Better and Best: {sol.kth_smallest_in_bst_better(root, 2)}')
    
    
    #Complexity ==> O(n)
