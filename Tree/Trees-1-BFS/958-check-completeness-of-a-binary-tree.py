# from typing import Optional, List
from collections import deque
import math


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
    def check_completeness_of_a_binary_tree(self, root :BinaryTreeNode):
        if not root:
            return False
        
        queue = deque([root])
        level = 1
        
        while queue:            
            #child_at_level_count = 0;
            node_cnt = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                node_cnt += 1
                

                if node.left:
                    queue.append(node.left)
                    #child_at_level_count += 1
                
                if node.right:
                    queue.append(node.right)
                    #child_at_level_count += 1            
            expected_node_cnt = math.pow(2,level-1)   
            print (f'level:{level} - node_cnt :{node_cnt} - 2^level:{expected_node_cnt}')
            if node_cnt != expected_node_cnt :                
                return False
            
            level += 1
        
        return True
        
    ## Grok            
    def check_completeness_of_a_binary_tree2(self, root :BinaryTreeNode):
        if not root:
            return True 
        
        queue = deque([root])
        
        seen_null = False
        
        while queue:
            
            node = queue.popleft()
            
            if node is None:
                seen_null = True
            else:
                if seen_null:
                    return False
                
                queue.append(node.left)
                queue.append(node.right)
            
        return True
        
    #OMKAR
    def check_completeness_of_a_binary_tree3(self, root :BinaryTreeNode):
        if not root:
            return True 
        
        queue = deque([root])        
        gap_flag=False
        
        while queue:            
            for _ in range(len(queue)):
                node = queue.popleft()
                print(f'{node.val} - {gap_flag}')
                
                if node.left:
                    queue.append(node.left)
                    if gap_flag == True:
                        return False
                else:
                    gap_flag= True
                    print(f'    left =>{node.val} - {gap_flag}')
    
                
                if node.right:
                    queue.append(node.right)
                    if gap_flag == True:
                        return False
                else:                    
                    gap_flag=True
                    print(f'    right =>{node.val} - {gap_flag}')
                
        
        return True


if __name__ == "__main__":
    values = [4,2,6,3,1,5,8] 
    
    sol = Solution()
    
    print('values = [4,2,6,3,1,5,8]')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    is_complete_binary_tree = sol.check_completeness_of_a_binary_tree(root)    
    print(is_complete_binary_tree) 
    
    print('------------------------------------------')
    
    values = [4,2,6,3,1,5] 
    
    sol = Solution()
    
    print('values = [4,2,6,3,1,5]')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    is_complete_binary_tree = sol.check_completeness_of_a_binary_tree(root)    
    print(is_complete_binary_tree) 
    
    print('------------------------------------------')
    
    values = [4,2,6,3,1, None,5] 
    
    sol = Solution()
    
    print('values = [4,2,6,3,1,None,5]')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    is_complete_binary_tree = sol.check_completeness_of_a_binary_tree(root)    
    print(is_complete_binary_tree) 
    
    print('------------------------------------------')
    
    values = [4,2,6,3,1, None, 5] 
    
    sol = Solution()
    
    print('values = [4,2,6,3,1,None,5]')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    is_complete_binary_tree = sol.check_completeness_of_a_binary_tree2(root)    
    print(is_complete_binary_tree) 

    print('------------------------------------------')
    
    values = [4,2,6,3] 
    
    sol = Solution()
    
    print('values = [4,2,6,3]')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    is_complete_binary_tree = sol.check_completeness_of_a_binary_tree2(root)    
    print(is_complete_binary_tree)     
    print('------------------------------------------')
    
    values = [4,2,6,3] 
    
    sol = Solution()
    
    print('values = [4,2,6,3]')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    is_complete_binary_tree = sol.check_completeness_of_a_binary_tree3(root)    
    print(is_complete_binary_tree)        

    print('------------------------------------------')

    values = [4,2,6,3,1,5,8] 
    
    sol = Solution()
    
    print('values = [4,2,6,3,1,5,8]')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    is_complete_binary_tree = sol.check_completeness_of_a_binary_tree3(root)    
    print(is_complete_binary_tree) 
    
    print('------------------------------------------')
    
    values = [4,2,6,3,1,5] 
    
    sol = Solution()
    
    print('values = [4,2,6,3,1,5]')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    is_complete_binary_tree = sol.check_completeness_of_a_binary_tree3(root)    
    print(is_complete_binary_tree) 
    
    print('------------------------------------------')
    
    values = [4,2,6,3,1, None,5] 
    
    sol = Solution()
    
    print('values = [4,2,6,3,1,None,5]')    
    root = build_binary_tree2(values)      
    print_tree(root) 
    
    is_complete_binary_tree = sol.check_completeness_of_a_binary_tree3(root)    
    print(is_complete_binary_tree)     