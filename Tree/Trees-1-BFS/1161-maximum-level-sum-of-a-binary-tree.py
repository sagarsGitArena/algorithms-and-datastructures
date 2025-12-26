# from typing import Optional, List
from collections import deque


# --------------------------
# TreeNode definition
# --------------------------

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left=left
        self.right=right



# --------------------------
# Print tree sideways
# --------------------------
def print_tree(node: TreeNode | None, prefix: str = "", is_left: bool = True):
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
        
        
        
##Input: [3, 9, 20, None, None, 15, 7]

def build_tree(values : list):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i >= len(values):
            break
        
        if values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
        
    return root


class Solution:
    def maximum_level_sum(self, root :TreeNode):
        if not root:
            return 0
        
        queue = deque([root])
        level=1
        result = 0
        hashmap = {}
        
        result = []
        while queue:            
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)                
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
        
        
        max_val = 0
        max_lvl= 0
        for i in range(len(result)):
            if max(result[i]) > max_val:            
                max_val = max(result[i])
                max_lvl = i+1
            
        
        return max_lvl

    def maximum_level_sum2(self, root :TreeNode):
        if not root:
            return 0
        
        queue = deque([root])
        
        max_level_sum = float("-inf")
        
        level = 0
        min_level = -1
        while queue:            
            level_sum = 0
            level += 1
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                level_sum += node.val                               
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_level_sum:
                max_level_sum = level_sum
                min_level = level
            
        return min_level
        
  
            
       
            
        
if __name__ == "__main__":
    values = [3,9, 20,None, None, 15, 7]
    values = [2, None, 3, None, 4, None, 5, None, 6]
    
  
    root = build_tree(values)      
    print_tree(root)       

    
    sol = Solution()
    output = sol.maximum_level_sum(root)
    
    print("Input:", values)
    print("Level Order Traversal:", output)     
    
    sol2 = Solution()
    output2 = sol2.maximum_level_sum2(root)
    
    print("Input:", values)
    print("Level Order Traversal:", output2)       
        