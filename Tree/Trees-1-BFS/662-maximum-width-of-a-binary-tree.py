from collections import deque
import math


# --------------------------
# TreeNode definition
# --------------------------

class BinaryTreeNode:
    def __init__(self, val=0, id=0,left=None, right=None):
        self.val = val
        self.id = id
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




def build_binary_tree(values : list):
    
    if not values:
        return 
        
    root = BinaryTreeNode(values[0])
    queue = deque([root])
    i = 0
    while queue and (i < len(values)):
        
        right_idx = (2 * i) + 1
        left_idx = (2 * i) + 2
        
        node = queue.popleft()
        print(node.val)
        
        if  right_idx < len(values) and values[right_idx]:
            node.right = BinaryTreeNode(values[right_idx])
            queue.append(node.right)

        if  left_idx < len(values) and values[left_idx]:
            node.left = BinaryTreeNode(values[left_idx])
            queue.append(node.left)
        
        i += 1
    
    return root


#values = [3, None, 20, None, None, 16, 7]
# The algorithm wouldnt work for the above values.
# The only way to work for the above input is to change the input as follows
# values = [3, None, 20, 16, 7]...makes sense ..since there is not left child to 3. Subsequently there wouldnt be any left and right childern to 3is  left child as its already None
def build_binary_tree2(values : list):
    
    if not values:
        return 
        
    root = BinaryTreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and (i < len(values)):
        
        node = queue.popleft()

        if  i < len(values) and values[i]:
            node.left = BinaryTreeNode(values[i])
            queue.append(node.left)

        i +=1 
        
        if  i < len(values) and values[i]:
            node.right = BinaryTreeNode(values[i])
            queue.append(node.right)
        
        i += 1
    
    return root

class Solution:
    ## This is my incorrect solution
    def max_width_of_binary_tree(self, root :BinaryTreeNode):
        if not root:
            return 0
        
        root.id = 1
        queue = deque([root])
        max_width = float("-inf")
        
        while queue:
            left_node_id = None
            right_node_id = 0
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if left_node_id is None:
                    left_node_id = node.id
                    
                right_node_id = node.id
                
                
                if node.left:
                    left_node = node.left
                    left_node.id = node.id * 2
                    queue.append(left_node)
                
                if node.right:
                    right_node = node.right
                    right_node.id = (node.id * 2) + 1
                    queue.append(right_node)
            
            max_width = max(max_width, right_node_id - left_node_id + 1)
            
        return max_width


if __name__ == "__main__":
    values = [1,3,2,5,3,None,9] 
    
    sol = Solution()
    
    print('  values = [1,3,2,5,3,None,9]')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    max_width= sol.max_width_of_binary_tree(root)    
    print(max_width) 
    
    print('------------------------------------------')
    
    values = [1,3,2,5,None,None,9,6,None,7] 
    
    sol = Solution()
    
    print('values = [1,3,2,5,None,None,9,6,None,7] ')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    max_width= sol.max_width_of_binary_tree(root)    
    print(max_width) 
    
    print('------------------------------------------')
    values = [1,3,2,5]
    
    sol = Solution()
    
    print('values = [1,3,2,5] ')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    max_width= sol.max_width_of_binary_tree(root)    
    print(max_width) 
    
    print('------------------------------------------')