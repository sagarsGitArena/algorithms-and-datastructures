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
    
    
    def convert_bst_to_sorted_doubly_linked_list(self, root: BinaryTreeNode):
        dummy = BinaryTreeNode();       
        prev_ptr = dummy
        
        def helper(node : BinaryTreeNode):
            nonlocal  prev_ptr
            
            if not node:
                return
            
            helper(node.left)
            
            prev_ptr.right = node
            node.left = prev_ptr
            prev_ptr =  node
        
                        
            helper(node.right)
    
        helper(root)
        
        head = dummy.right
        
        if head:
            head.left = None
        
        return head



def print_doubly_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" <-> " if curr.right else "")
        curr = curr.right
    print()



class TestMySelf:
    
    def convert_bst_to_sorted_doubly_linked_list(self, root: BinaryTreeNode):
        dummy = BinaryTreeNode()
        current_ptr = dummy
        
        
        def helper(node : BinaryTreeNode):
            nonlocal current_ptr
            
            if not node:
                return
            
            helper(node.left)
            
            node.left = current_ptr
            current_ptr.right = node
            current_ptr = current_ptr.right
            
            helper(node.right)
        
        
        helper(root)
        head = dummy.right
        if head:
            head.left = None
        
        return head
        


if __name__ == "__main__":
    values = values = [5,3,6,2,4,None,8]
    
    
    root = build_tree(values)      
    print_tree(root)    
    
    # sol = Solution()
    # print_doubly_linked_list(sol.convert_bst_to_sorted_doubly_linked_list(root))
    sol = TestMySelf()
    print_doubly_linked_list(sol.convert_bst_to_sorted_doubly_linked_list(root))
