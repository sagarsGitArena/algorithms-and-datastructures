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
    
    def balanced_binary_tree_vertices_based_solution_optimal_solution(self, root: BinaryTreeNode):

        
        def helper(node : BinaryTreeNode):            
            if not node :
                return 0
            
            left_height = helper(node.left)
            if left_height == -1:
                return -1
            
            right_height = helper(node.right)
            if right_height == -1:
                return -1
            
            # print(f'heights: {left_height} -- {right_height}')
            
            height_diff = left_height - right_height            
            
            # print (f'height diff at Node {node.val} --> {height_diff}')
            if abs(height_diff) > 1:
                return -1
                
            
            return max(right_height, left_height) + 1
        
        
        
        return helper(root) != -1

    def balanced_binary_tree_vertices_based_solution_suboptimal_solution(self, root: BinaryTreeNode):
        isBalanced = True
        
        def helper(node : BinaryTreeNode):
            nonlocal isBalanced
            
            if not node :
                return 0
            
            left_height = helper(node.left)
            
            right_height = helper(node.right)

            ## Actual work done here
            # print(f'heights: {left_height} -- {right_height}')
            
            height_diff = left_height - right_height            
            
            #print (f'height diff at Node {node.val} --> {height_diff}')
            if abs(height_diff) > 1:
                isBalanced = False               
            
            return max(right_height, left_height) + 1
        

    
        helper(root)
        return isBalanced
        


    def balanced_binary_tree_edge_based_solution(self, root: BinaryTreeNode):
        
        return


if __name__ == "__main__":
    values = [3,9,20,None,None,15,7]
    
    values = [1,2,2,3,3,None, None,4,4]
    
    values = [1,2,3,4,5,6, None,8,9,10, 11, 12, 13,None,None,None,20, None,None,25]

    #values = [3,9]
    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    print(f'Optimal : {sol.balanced_binary_tree_vertices_based_solution_optimal_solution(root)}')
    
    print(f'Sub - Optimal : {sol.balanced_binary_tree_vertices_based_solution_suboptimal_solution(root)}')
