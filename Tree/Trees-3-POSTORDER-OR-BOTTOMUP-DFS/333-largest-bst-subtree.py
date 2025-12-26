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
    
    
    def largest_BST_subtree(self, root: BinaryTreeNode):
        global_max = float("-inf")
        global_max_bst = BinaryTreeNode(None)
        
        
        def helper(node : BinaryTreeNode, min :int, max:int):
            nonlocal global_max
            nonlocal global_max_bst
            
            is_bst = False
            cnt = 0
            
            if not node:
                return (True, 0)
            
            if not (min < node.val < max ):
                return (False, 0)
            
            (is_left_bst, left_count) = helper(node.left, min, node.val)
            (is_right_bst, right_count) = helper(node.right, node.val, max)
            
            print(f'{is_left_bst} ------  {is_right_bst}')
            if is_left_bst and is_right_bst:
                cnt = left_count + right_count + 1       
                is_bst = True                        
                if cnt > global_max:
                    global_max_bst = node 
                    global_max = cnt           
            
            return (is_bst, cnt)    
            

    
        helper(root, float("-inf"), float("inf"))
        return global_max

    def largest_bst_subtree_bottom_up(self, root: BinaryTreeNode):
        max_size = 0
        
        def dfs(node : BinaryTreeNode):
            nonlocal max_size
            
            if not node:
                return (True, 0, float("Inf"), float("-Inf"))
            
            (is_left_subtree_bst, left_size, left_min, left_max) = dfs(node.left)
            (is_right_subtree_bst, right_size, right_min, right_max) = dfs(node.right)
            
            is_bst = (is_left_subtree_bst and is_right_subtree_bst) and ( left_max < node.val < right_min)
            
            if is_bst:
                curr_size = left_size + right_size + 1
                max_size  = max(max_size, curr_size)
                return (is_bst, max_size, min(left_min, node.val), max(node.val, right_max))
            
            else:
                max_sub_size = max(left_size, right_size)
                return (is_bst, max_sub_size,  0, 0)
        
        dfs(root)
        return max_size


if __name__ == "__main__":
    values = [10,5,15,1,8,None,7]
    values = [4,2,7,2,3,3,None,2,None,None,None,None,None,1]
    
    
    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    print(f'BAD solution(:()  ==> {sol.largest_BST_subtree(root)}')
    print(f'Optimal (:)) ==> {sol.largest_bst_subtree_bottom_up(root)}')

