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
    
    
    def validate_binary_search_tree(self, root: BinaryTreeNode):
        
        def helper(node : BinaryTreeNode, low:int, high: int):
            is_left_subtree_bst = False
            is_right_subtree_bst = False
            
            
            
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            print(f'[{node.val}] -- [{low}] -- [{high}]')
            
            is_left_subtree_bst = helper(node.left, low, node.val)
                
            is_right_subtree_bst = helper(node.right, node.val, high)
            
            #print(f'{is_left_subtree_bst} ----- {is_right_subtree_bst}')
            
            if is_left_subtree_bst and is_right_subtree_bst:
                return True
            
        return helper(root, float("-Inf"), float("Inf"))
        

    def validate_binary_search_tree_bottom_up(self, root: BinaryTreeNode):
        
        def dfs(node : BinaryTreeNode):
            
            if not node:
                return (True, float("Inf"), float("-Inf"))
            
            (is_left_subtree_bst, left_min, left_max) = dfs(node.left)
            (is_right_subtree_bst, right_min, right_max) = dfs(node.right)
            
            is_bst = (is_left_subtree_bst and is_right_subtree_bst) and ( left_max < node.val < right_min)
            
            if is_bst:
                return (is_bst, min(left_min, node.val), max(node.val, right_max))
            else:
                return (is_bst, 0, 0)
        
        (is_bst, _, _) = dfs(root)
        return is_bst


if __name__ == "__main__":
    values = [5,1,4,None, None, 3,6]
    #values = [2,1,3]
    values = [4,1,6,None, None, 5,8]
    values = [7,4,10,2,6,8,12]
    
    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    print(f'Optimal : {sol.validate_binary_search_tree(root)}')
    
    sol = Solution()
    print(f'Optimal : {sol.validate_binary_search_tree_bottom_up(root)}')
