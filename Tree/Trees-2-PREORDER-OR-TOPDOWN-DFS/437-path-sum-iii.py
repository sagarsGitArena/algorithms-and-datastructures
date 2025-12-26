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
    
    def path_sum3(self, root: BinaryTreeNode, targetSum: int):
        path_count = 0
        
        
        def helper(node: BinaryTreeNode, target_sum :int, current_sum :int):
            nonlocal path_count
            
            
            
            current_sum += node.val
            
         
            
            print(f'node visited: {node.val} :current_sum:{current_sum}')
            
            if current_sum == target_sum:
                print(f'target sum  reached :{node.val}')
                path_count += 1
            
            if current_sum > target_sum:
                current_sum = node.val
               
            if not node.left and not node.right:
                return
            
            if node.left:
                if (current_sum < target_sum):
                    if (current_sum + node.left.val) > target_sum :
                        current_sum = node.val
                helper(node.left, target_sum, current_sum )
            
            if node.right:
                if (current_sum < target_sum):
                    if (current_sum + node.right.val) > target_sum :
                        current_sum = node.val
                helper(node.right, target_sum, current_sum)
        
        helper(root, target_sum, 0)
        return path_count
        
        
if __name__ == "__main__":
    values = [10,5,-3,3,2,None,11,3,-2, None,1]
    
    target_sum= 8


    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    results = sol.path_sum3(root, target_sum)
    print(results)
    print('------------------------------------------------')
    values = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    target_sum = 22

    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    results = sol.path_sum3(root, target_sum)
    print(results)