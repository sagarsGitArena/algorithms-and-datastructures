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
    
    def add_row_to_binary_tree(self, root :BinaryTreeNode, val:int, depth:int):
        if not root:
            return None
        
        queue = deque([root])
        level = 1
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if level == depth:
                    new_left_node = BinaryTreeNode(val)
                    new_right_node = BinaryTreeNode(val)
                    new_left_node.left = node.left
                    new_right_node.right = node.right
                    node.left = new_left_node
                    node.right = new_right_node
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
        
        return root
                
            
        
        
        



if __name__ == "__main__":
    values = [4,2,6,3,1,5] 
    val=1 
    depth=4 

    
    sol = Solution()
    
    print('values = [4,2,6,3,1,5] val=1 and depth=4 ')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    root = sol.add_row_to_binary_tree(root, val, depth)     
    
    print_tree(root)
    
    print('------------------------------------------')
    values = [4,2,None,3,1] 
    val=1
    depth=3

    print('values = [4,2,None,3,1]  val=1 and depth=3 ')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    root = sol.add_row_to_binary_tree(root, val, depth)     
    
    print_tree(root)
    
    print('------------------------------------------')