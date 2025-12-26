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
    
    
    def recover_bst(self, root: BinaryTreeNode):
        first = second = prev = None
        def helper(node : BinaryTreeNode):
            nonlocal first, second, prev
            print('------------------------------')
            
            
            if not node:
                return
            
            helper(node.left)
            
            if prev and node.val  < prev.val:
                if not first:
                    first = prev
                second = node

            if prev:
                print(f'previous :{prev.val}')

            print(f'\t node:- {node.val}')
                       
            if  first:
                print(f'first :{first.val}')
            if  second:
                print(f'second :{second.val}')
            prev = node 
            helper(node.right)
            
            
        helper(root)
        first.val, second.val = second.val, first.val


class SeflCheck:
    
    
    def recover_bst(self, root: BinaryTreeNode):
        first = second = prev = None
        def helper(node: BinaryTreeNode):
            nonlocal first, second, prev
            
            if not node:
                return
            
            helper(node.left)
            
            if prev and node.val < prev.val:
                if not first:
                    first = prev                
                second = node
            
            prev = node
            helper(node.right)
            
        
        helper(root)
        first.val, second.val = second.val, first.val
        
        
if __name__ == "__main__":
    values = [1,3, None, None,2]
    #values = [3,1,4,None,None,2]
    values = [5,3,7,2,8,6,4,1]
    
    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    sol.recover_bst(root)
    print_tree(root) 

#INPUT:
# │       ┌── 4
# │   ┌── 7
# │   │   └── 6
# └── 5
#     │   ┌── 8
#     └── 3
#         └── 2
#             └── 1

#OUTPUT:
# │       ┌── 8
# │   ┌── 7
# │   │   └── 6
# └── 5
#     │   ┌── 4
#     └── 3
#         └── 2
#             └── 1