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


def print_tree_top_down(root: TreeNode | None):
    if not root:
        print("Empty tree")
        return

    # Perform BFS to collect nodes level by level
    levels = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_nodes = []
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                level_nodes.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level_nodes.append(None)
                queue.append(None)
                queue.append(None)
        # Check if all nodes in this level are None
        if all(n is None for n in level_nodes):
            break
        levels.append(level_nodes)

    # Calculate spacing for pretty print
    max_width = len(levels[-1]) * 4
    for i, level in enumerate(levels):
        spacing = int(max_width / pow(2, i + 1))
        line = ""
        for val in level:
            if val is None:
                line += " " * spacing
            else:
                line += f"{val}".center(spacing)
        print(line.center(max_width))


# --------------------------
# Build a tree from list (level order)
# Example: [1, 2, 3, None, 4]
# --------------------------

##Input: [3, 9, 20, None, None, 15, 7]


#values = [3,9, 20,None, None, 15, 7]
def build_binary_tree_recursive(values : list, i=0):
    
    if i > len(values) or values[i] is None:
        return 
    
    node = TreeNode(values[i])
    node.left = build_binary_tree_recursive(values, i*2+1)
    node.right = build_binary_tree_recursive(values, i*2+2)
    
    return node
  
  #values = [3, None, 20, None, None, 16, 7]
# The algorithm wouldnt work for the above values.
# The only way to work for the above input is to change the input as follows
# values = [3, None, 20, 16, 7]...makes sense ..since there is not left child to 3. Subsequently there wouldnt be any left and right childern to 3is  left child as its already None
def build_binary_tree2(values : list):
    
    if not values:
        return 
        
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and (i < len(values)):
        
        node = queue.popleft()
        print(f'idx : {i} -- value {node.val}')
       
        
        if  i < len(values) and values[i]:
            node.left = TreeNode(values[i])
            queue.append(node.left)

        i +=1 
        
        if  i < len(values) and values[i]:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        
        i += 1
    
    return root
    
class Solution:  
# --------------------------
# Level Order Traversal or BFS
# --------------------------
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        queue = deque([root])
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
            
            
         #   if not level:
            result.append(level)
        
        return result
    
    
#
# Bottom up level order traversal
#    
# Leet Code 107
#
    def bottomUpLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        queue = deque([root])
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
            print(result)
            
        #print(result[::-1])
        
       # result.reverse()
         
        return result[::-1]


    def bottomUpLevelOrder2(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        queue = deque([root])
        result = deque ([])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.appendleft(level)
            print(result)
        return list(result)
            
            
## driver code

if __name__ == "__main__":
    values = [3,9, 20,None, None, 15, 7]
    values = [3, None, 20, None, None, 16, 7]
    
  
       
    root = build_binary_tree(values)  
    print_tree(root)       
    
    
    sol = Solution()
    output = sol.levelOrder(root)
    
    print("Input:", values)
    print("Level Order Traversal:", output)
    
    # print('--------------------------------------')
    # print(root.val)
    # output2 = sol.bottomUpLevelOrder2(root)
    # print("Input:", values)
    # print("Bottom Up Level Order Traversal:", output2)