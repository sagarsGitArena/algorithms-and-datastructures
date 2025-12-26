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
    
    def cousins_in_binary_tree(self, root :BinaryTreeNode, x:int, y:int):
        if not root:
            return False
        
        queue = deque([root])
        level = 0
        x_level = 0
        y_level = 0
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()                
                
                if node.val == x:
                    x_level = level
                
                if node.val == y:
                    y_level = level
                    
                if node.left: 
                    queue.append(node.left)
                    left_node = node.left
                    if node.left.val == x:
                        px = node.val
                    if node.left.val == y:
                        py = node.val                    
                    
                if node.right:
                    queue.append(node.right)
                    right_node = node.right
                    if node.right.val == x:
                        px = node.val
                    if node.right.val == y:
                        py = node.val                    
                    
        if x_level == y_level and px != py:
            return True
        else:
            return False




if __name__ == "__main__":
    values = [1,2,3,4,]
    x=3
    y=4

     
    
    sol = Solution()
    
    print('values = [1,2,3,4,] x=3 and y=4 ')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    are_cousins = sol.cousins_in_binary_tree(root, x, y)     
    print(are_cousins)        
    
    print('------------------------------------------')
    
    print('values = [1,2,3,None,4,None,5] x=5 and y=4 ')   
    values = [1,2,3,None,4,None,5] 
    x=5
    y=4 
    root = build_binary_tree2(values)      
    print_tree(root)  
    are_cousins = sol.cousins_in_binary_tree(root, x, y)     
    print(are_cousins)        
    
    print('------------------------------------------')    
    print('values = [1,2,3,None,4] x=2 and y=3')   
    values = [1,2,3,None,4] 
    x=2
    y=3 
    root = build_binary_tree2(values)      
    print_tree(root)  
    are_cousins = sol.cousins_in_binary_tree(root, x, y)     
    print(are_cousins)    
        


        
        
