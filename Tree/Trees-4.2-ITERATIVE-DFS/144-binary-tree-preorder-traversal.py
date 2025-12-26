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
    
    
    def preorder_traversal_recursive(self, root: BinaryTreeNode):
        preorder_list = []
        
        def helper(node : BinaryTreeNode):
            nonlocal preorder_list
            
            if not node:
                return
            
            
            preorder_list.append(node.val)
            helper(node.left)
            helper(node.right)
    
        helper(root)   
        return preorder_list
    
    def iterative_traversal(self, root: BinaryTreeNode):
        stack = []
        stack.append(root)
        
        while len(stack) > 0:
            for i in stack:
                print(i.val)
                
            node = stack.pop()
            if node.left:                
                stack.append(node.left)            
            if node.right:                
                stack.append(node.right)
            #else:
                
            print('----------------')
            
            
            
            
        

    def preorder_traversal_iterative(self, root: BinaryTreeNode):
        result = []
        stack = []
        stack.append((root, "pre"))
        
        while len(stack) > 0:
            ## peek at the right most or last element of the stack/list
            (node, zone) = stack[-1]
            
            if zone == "pre":
                ####### ACTUAL WORK #######
                result.append(node.val)
                ###########################
                stack[-1] = (node, "in")                
                if node.left:
                    stack.append((node.left, "pre"))
            elif zone == "in":
                stack[-1] = (node, "post")
                if node.right:
                    stack.append((node.right, "pre"))
            else: ## zone = "post"
                stack.pop()
                
                
        return result
                
                    
                
            
           
        



if __name__ == "__main__":
    values = [3,9,20,None,None,15,7]
    values = [1,2,3,4,5,None,8,None,None,6,7,9]
    
    
    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    #sol.iterative_traversal(root)
    print(f'recursive : {sol.preorder_traversal_recursive(root)}')
    
    print(f'iterative : {sol.preorder_traversal_iterative(root)}')
