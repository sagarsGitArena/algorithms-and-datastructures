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




def build_binary_tree(values : list):
    
    if not values:
        return 
        
    root = BinaryTreeNode(values[0])
    queue = deque([root])
    i = 0
    while queue and (i < len(values)):
        
        right_idx = (2 * i) + 1
        left_idx = (2 * i) + 2
        
        node = queue.popleft()
        print(node.val)
        
        if  right_idx < len(values) and values[right_idx]:
            node.right = BinaryTreeNode(values[right_idx])
            queue.append(node.right)

        if  left_idx < len(values) and values[left_idx]:
            node.left = BinaryTreeNode(values[left_idx])
            queue.append(node.left)
        
        i += 1
    
    return root


#values = [3, None, 20, None, None, 16, 7]
# The algorithm wouldnt work for the above values.
# The only way to work for the above input is to change the input as follows
# values = [3, None, 20, 16, 7]...makes sense ..since there is not left child to 3. Subsequently there wouldnt be any left and right childern to 3is  left child as its already None
def build_binary_tree2(values : list):
    
    if not values:
        return 
        
    root = BinaryTreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and (i < len(values)):
        
        node = queue.popleft()
        print(f'idx : {i} -- value {node.val}')
       
        
        if  i < len(values) and values[i]:
            node.left = BinaryTreeNode(values[i])
            queue.append(node.left)

        i +=1 
        
        if  i < len(values) and values[i]:
            node.right = BinaryTreeNode(values[i])
            queue.append(node.right)
        
        i += 1
    
    return root

class Solution:
    
    def univalued_binary_true(self, root: BinaryTreeNode):
        if not root:
            return False        
        
        queue = deque([root])
        
        val= root.val
        
        
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.val != val:
                    return False
                
                if node.left:                                   
                    queue.append(node.left)
            
                if node.right:                                    
                    queue.append(node.right)
            
        
        return True


if __name__ == "__main__":
    values = [ 1,1,1,1,1,None,1]
    
  
       
    root = build_binary_tree2(values) 
    print_tree(root)  
    sol = Solution()
    
    print(sol.univalued_binary_true(root))
    