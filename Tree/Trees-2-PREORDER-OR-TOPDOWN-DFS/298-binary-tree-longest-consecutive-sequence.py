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
    
    def leet_code_298_binary_tree_longest_consecutive_sequence(self, root: BinaryTreeNode):
        
        global_max = 1
        
        
        def helper(node: BinaryTreeNode, parent_node_val: int, seq_cnt: int):
            nonlocal global_max
            if not node:
                return None
            
            if (node.val - parent_node_val ==1):
                seq_cnt += 1
            else:
                seq_cnt = 1
            
            global_max = max(seq_cnt, global_max)
            
            helper2(node.left, node.val, seq_cnt)
            helper2(node.right, node.val, seq_cnt)
        
        helper2(root, root.val -1, 1)
        return global_max




if __name__ == "__main__":
    values = [1,None,3,2,4,None,None,None,5]
    #values = [2,None,3,2,None,1]
    #values = [2,None,3,2,1,4]

    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    results = sol.leet_code_298_binary_tree_longest_consecutive_sequence(root)
    print(results)
    # print(len(results))
        