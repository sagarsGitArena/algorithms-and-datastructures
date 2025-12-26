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
    
    
    def increasing_order_search_tree(self, root: BinaryTreeNode):
        new_root =  BinaryTreeNode()
        current_node_ptr = new_root
        
        def helper(node : BinaryTreeNode): 
            nonlocal current_node_ptr   
            
            if not node:
                return        
                
            helper(node.left)
            

            current_node_ptr.right =  node
            current_node_ptr = node
            node.left = None 

        
        
            helper(node.right)
    
        helper(root)      
        return new_root.right




class CheckingMySelf:
    
    
    def increasing_order_search_tree(self, root: BinaryTreeNode):
        
        dummy = BinaryTreeNode()
        current_ptr = dummy
        
        def helper(node: BinaryTreeNode):
            nonlocal current_ptr
            
            if not node:
                return
            
            helper(node.left)
            
            node.left = None
            current_ptr.right = node
            current_ptr = current_ptr.right
            
            
            helper(node.right)
        
        helper(root)
        return dummy.right












if __name__ == "__main__":
    
    
    values = [2,1, None]
    values = [4,2, None,1,3]
    values = [5,3,6,2,4,None,8]
    
    
    root = build_tree(values)      
    print_tree(root)    
    
    # sol = Solution()
    # print_tree(sol.increasing_order_search_tree(root))
    # print(f'Time Complexity : O(n)')
    # print(f'Space Complexity : O(h) best case. Worst case O(n) ')
    sol2 = CheckingMySelf()
    print_tree(sol2.increasing_order_search_tree(root))
    print(f'Time Complexity : O(n)')
    print(f'Space Complexity : O(h) best case. Worst case O(n) ')
    
