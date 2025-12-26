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

def build_tree(values : list[int | None]) -> TreeNode | None:
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
# --------------------------
# average of levels in binary tree
# --------------------------
    def avg_of_levels_levelOrder(self, root: TreeNode):
        if not root:
            return []
        
        result = []        
        queue = deque([root])        
        avg_of_levels = []
        
        while queue:
            levels = []
            
            for _ in range(len(queue)):      
                node = queue.popleft()  
                levels.append(node.val)              
                
                if node.left:                    
                    queue.append(node.left)                    
                    
                
                if node.right:              
                    queue.append(node.right)                    
                
            result.append(levels)
            if len(levels) > 0:
                avg = sum(levels)/len(levels)
                avg_of_levels.append(avg)

        return  avg_of_levels        
    
                
    def avg_of_levels_levelOrder2(self, root: TreeNode):
        if not root:
            return []
        
        result = []        
        queue = deque([root])        
        
        while queue:       
            sum = 0
            length = 0
            
            for i in range(len(queue)):      
                node = queue.popleft()  
                sum += node.val
                length += 1
                
                if node.left:                    
                    queue.append(node.left)                    
                    
                
                if node.right:              
                    queue.append(node.right)                    

            result.append(sum/length)
        return  result   


if __name__ == "__main__":
    values = [3,9, 20,None, None, 15, 7]

    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    avg_of_levels_levelOrder = sol.avg_of_levels_levelOrder(root)     
    print(avg_of_levels_levelOrder)
    
    avg_of_levels_levelOrder2 = sol.avg_of_levels_levelOrder2(root)    
    print(avg_of_levels_levelOrder2)