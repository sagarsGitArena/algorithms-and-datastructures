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
            if node:
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
# #values = [3,None, 20,16,7]    
def build_tree(values : list):
    if not values:
        return
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
                

        if values[i]:
            node.left = TreeNode(values[i])
            print(f' 1-> {values[i]}')
            queue.append(node.left)
            i += 1
            

        if values[i]:
            node.right = TreeNode(values[i])
            print(f' 2-> {values[i]}')
            queue.append(node.right)
            i += 1
        
        i += 1
            
    return root 

class Solution:   
# largest value in each tree row
    def minimum_depth_of_a_binary_tree( self, root : TreeNode):
        
        if not root:
            return 0        
        
        min_depth = 0       
        queue = deque([root])
                
        while queue:
            
            min_depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return min_depth
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
                

        return min_depth                    
        
        


if __name__ == "__main__":
    values = [3,9, 20,None, None, 15, 7]
    values = [2, None, 3, None, 4, None, 5, None, 6]
    
    values = [3,None, 20,16,7]
    
    

    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    results = sol.minimum_depth_of_a_binary_tree(root)
    print(results)
    
