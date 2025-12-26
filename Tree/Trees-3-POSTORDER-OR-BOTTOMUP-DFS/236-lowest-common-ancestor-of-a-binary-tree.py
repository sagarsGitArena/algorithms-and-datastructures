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
    
    
    
    
    def lowest_common_ancestor_of_a_binary_tree(self, root: BinaryTreeNode, p: int, q: int):
        lowest_common_ancestor = None
        def helper(node : BinaryTreeNode, p: int, q: int):
            nonlocal lowest_common_ancestor
            found_p = False
            found_q = False
            p_in_left_subtree = False
            q_in_left_subtree = False
            p_in_right_subtree = False
            q_in_right_subtree = False
            
            if lowest_common_ancestor:
                return (False, False)
            
            if not node:
                return (False, False)
            
            
            if node.left:            
                (p_in_left_subtree, q_in_left_subtree) = helper(node.left, p, q)
            
            if node.right:
                (p_in_right_subtree, q_in_right_subtree) = helper(node.right, p, q)
            
            if p_in_left_subtree or p_in_right_subtree or node.val == p :
                found_p = True
            
            if q_in_left_subtree or q_in_right_subtree or node.val == q :
                found_q = True
            
            if (found_p and found_q ) and not lowest_common_ancestor:
                lowest_common_ancestor = node.val

            print(f'{node.val} - {found_p} & {found_q}')
            
            
            return(found_p, found_q)
            

        helper(root, p, q) 
        return lowest_common_ancestor 
        

    
if __name__ == "__main__":
    values = [3,5,1,6,2,0,8,None, None,7,4]
    p = 5
    q = 4
    
    
    root = build_tree(values)      
    print_tree(root)    
    print(f'p:{p} \t q:{q}')
    sol = Solution()
    print(f'Optimal : {sol.lowest_common_ancestor_of_a_binary_tree(root, p, q)}')
