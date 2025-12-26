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
    def path_sum(self, root: BinaryTreeNode, target_sum: int):
        
        calculated_sum = 0
        global_result = False
        def helper(node: BinaryTreeNode, target_sum:int, calculated_sum: int):
            nonlocal global_result
            print(node.val)
            calculated_sum += node.val

            if not node.left and not node.right:
                if calculated_sum == target_sum:
                    global_result = True

            
            # print(f'node: {node.val} sum:{calculated_sum}')
            if node.left:
                helper(node.left, target_sum, calculated_sum)
            
            if node.right:
                helper(node.right, target_sum, calculated_sum)
        
        helper(root, target_sum, 0)
        
        return global_result

    
    
    
if __name__ == "__main__":
    values = [5,4,8,11, None,13,4,7,2,None,None,None,1]
    target_sum= 22




    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    results = sol.path_sum(root, target_sum)
    print(results)
        