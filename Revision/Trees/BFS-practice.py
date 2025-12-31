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

class BinaryTreeNodeWithId:
    def __init__(self,val=0, left=None, right=None):
        self.id= 0
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


class NaryTreeNode:
    def __init__(self, val: int = 0, children: list["NaryTreeNode"] | None = None):
        self.val = val
        # Use empty list if children not provided
        self.children = children if children is not None else []

    def __repr__(self):
        return f"NaryTreeNode({self.val})"
    
#  values = [1, None, 3, 2, 4, None, 5,6]
##This is a working example
def build_nary_tree(values):
    if not values:
        return None
    
    # First value is the root
    root = NaryTreeNode(values[0])
    queue = deque([root])
    i = 1

    # BFS build
    while queue and i < len(values):
        parent = queue.popleft()
        
        if values[i] is None:
            i += 1


        # Add children until we hit None
        while i < len(values) and values[i] is not None:
            child = NaryTreeNode(values[i])
            parent.children.append(child)
            queue.append(child)
            i += 1


    return root



def print_nary_tree(root, level=0):
    if not root:
        return
    print("  " * level + f"- {root.val}")
    for child in root.children:
        print_nary_tree(child, level + 1)


class Solution:
    
    
    def leet_code_102_level_order_traversal(self, root: BinaryTreeNode):
        
        result = []
        queue = deque([root])
        
        while queue:
            level = []
            
            
            for _ in range(len(queue)):  
                node = queue.pop()
                level.append(node.val)             
                
                if node.left:
                    queue.appendleft(node.left)                    
                
                if node.right:
                    queue.appendleft(node.right)
                
            result.append(level)
                
        return result        

    def leet_code_199_right_side_view_of_binary_tree(self, root: BinaryTreeNode):
        if not root:
            return []
        
        result = []
        
        queue = deque([root])
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                #node = queue.pop()
                print(f' node val :{node.val}')
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    #queue.appendleft(node.left)
            
                if node.right:
                    queue.append(node.right)
                    #queue.appendleft(node.right)
             
            print (level)   
            result.append(level[-1])
        
        return result

    def leet_code_103_zigzag_lever_order_traversal(self, root: BinaryTreeNode):
        if not root:
            return []
        result = []
        
        queue = deque([root])
        i = 0
        while queue:
            level_order_list = []            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                level_order_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
                
            if i % 2 == 0:
                result.append(level_order_list)
            else:
                result.append(level_order_list[::-1])
            
            i += 1
                
            
        return result
    def leet_code_637_average_of_levels_in_binary_tree(self, root: BinaryTreeNode):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                
                node = queue.popleft()
                
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
            result.append(level_sum/level_size)
        
        return result

    def leet_code_104_max_depth_of_a_binary_tree(self, root: BinaryTreeNode):
        
        if not root:
            return 0
        
        queue = deque([root])
        max_depth =float("-inf")
        depth = 0
        while queue:
            depth += 1
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            max_depth = max(depth, max_depth)
        return max_depth

    def leet_code_111_min_depth_of_a_binary_tree(self, root: BinaryTreeNode):
        
        if not root:
            return 0
        
        queue = deque([root])
        min_depth =float("inf")
        depth = 0
        while queue:
            depth += 1
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            min_depth = min(depth, min_depth)
        return min_depth
    
    def leet_code_429_nary_levelorder_traversal(self, root:NaryTreeNode):
        if not root:
            return []
        
        result = []
        
        queue = deque([root])
        
        while queue:
            level = []
            for _ in range (len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.children:
                    children = node.children
                    for child in children:
                        queue.append(child)
            result.append(level)
        return result
    
    def leet_code_515_largest_value_in_tree_row(self, root: BinaryTreeNode):
        if not root:
            return []
        
        result = []
        
        queue = deque([root])
        
        while queue:
            max_in_row = float('-inf')            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                max_in_row = max(max_in_row, node.val)
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
            result.append(max_in_row)
        
        return result
    
    def leet_code_515_max_depth_of_nary_tree(self, root: NaryTreeNode):
        if not root :
            return 0
        
        max_depth = 0
        depth = 0
        
        queue = deque([root])
        
        while queue:
            depth += 1
            
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
            
            max_depth = max(max_depth, depth)
        return max_depth
    
    def leet_code_623_add_one_row_to_binary_tree(self, root: BinaryTreeNode, val: int, depth: int):
        
        queue = deque([root])
        
        if depth == 1:
            node = root            
            new_node = BinaryTreeNode(val)
            new_node.left = node
            
            root = new_node
            return root
            
        current_level = 0
        
        
        while queue:
            current_level += 1
            
            for _ in range(len(queue)):
                node = queue.popleft()
            
                if current_level == (depth -1):                                        
                    new_left_node = BinaryTreeNode(val)
                    new_left_node.left = node.left
                    node.left = new_left_node                    
                    
                    new_right_node = BinaryTreeNode(val)                    
                    new_right_node.right = node.right
                    node.right = new_right_node
                    
                else:                     
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    
        
        return root
    
    def leet_code_662_maximum_width_of_a_binary_tree(self, root: BinaryTreeNodeWithId):
        if not root:
            return 0
        root.id = 1
        queue = deque([root])
        max_width = 0
        
        
        while queue:              
            
            max_width = max(max_width, queue[-1].id -  queue[0].id +1)
            
            for _ in range (len(queue)):
                node = queue.popleft()
                id = node.id                
                
                if node.left:
                    left_node = node.left
                    left_node.id = 2 * id                    
                    queue.append(left_node)
                    
                if node.right:
                    right_node = node.right
                    right_node.id = 2 * id + 1                   
                    queue.append(right_node)
                    
                

            
        return max_width
    
    def leet_code_958_check_completeness_of_binary_tree(self, root: BinaryTreeNode):
                
        if not root:
            return False
        
        
        queue = deque([root])
        level = 0
        gap_flag = False
        while queue:
            
            num_nodes_at_level = len(queue)
            for _ in range(num_nodes_at_level):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                    if gap_flag == True:
                        return False

                else:
                    gap_flag = True
                    

                if node.right:
                    queue.append(node.right)
                    if gap_flag == True:
                        return False
                else:
                    gap_flag = True
            
        return True
        
    def leet_code_965_univalued_binary_tree(self, root: BinaryTreeNode):
        if not root:
            return True
        
        is_uni_val = True
        uni_value = root.val
        queue = deque([root])
        
        while queue:
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.val != uni_value:
                    is_uni_val = False
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return is_uni_val


    def leet_code_993_cousins_in_binary_Tree(self, root: BinaryTreeNode, p:int, q:int):
        if not root:
            return False
        is_cousins = False
   
        
        
        
        queue = deque([root])
        
        while queue:
            found_p = False
            found_q = False
            p_parent = None
            q_parent = None
            
            for _ in range(len(queue)):
                
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    if p == node.left.val:
                        found_p = True
                        p_parent = node.val
                    if q == node.left.val:
                        found_q = True
                        q_parent = node.val
                if node.right:
                    queue.append(node.right)
                    if p == node.right.val:
                        found_p = True
                        p_parent = node.val
                    if q == node.right.val:                        
                        found_q = True
                        q_parent = node.val
            
            if (found_q and found_p )  and p_parent != q_parent:
                is_cousins = True
                break
        
        return is_cousins     
    
    def leet_code_1161_max_level_sum_in_binary_Tree(self, root: BinaryTreeNode):
        
        if not root:
            return 0
        max_sum = float("-inf")
        result = 0
        
        queue = deque([root])
        level = 0
        while queue:
            level += 1
            level_sum = 0
            
            for _ in range(len(queue)):
                                
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
        
                if node.right:
                    queue.append(node.right)
            
            if level_sum > max_sum:
                max_sum = level_sum
                result = level
        
        return result
            
        

if __name__ == "__main__":
    
    values = [3,9,20,None,None,15,7]
    print(f'values = [3,9,20,None,None,15,7]')
    
    values = [4,2,6,3,1,5,None,None,None,None,None,9,3,10]
    
    root = build_tree(values)      
    print_tree(root)    
    sol = Solution()
    print(f'102- level order traversal : {sol.leet_code_102_level_order_traversal(root)}')
    print(f'199- right side view of bt : {sol.leet_code_199_right_side_view_of_binary_tree(root)}')
    print(f'103- zig zag level order traversal : {sol.leet_code_103_zigzag_lever_order_traversal(root)}')
    print(f'637- average of levels in bst : {sol.leet_code_637_average_of_levels_in_binary_tree(root)}')
    print(f'104- max depth of a binary tree : {sol.leet_code_104_max_depth_of_a_binary_tree(root)}') 
    print(f'111- min depth of a binary tree : {sol.leet_code_111_min_depth_of_a_binary_tree(root)}')
    print(f'515- largest value in each tree row : {sol.leet_code_515_largest_value_in_tree_row(root)}')  
    values = [1,2,3,4,5,6]
    root = build_tree(values)      
    print_tree(root)
    print(f'958- check completeness of a binary tree (REVISIT and REVISE): {sol.leet_code_958_check_completeness_of_binary_tree(root)}')   
    print(f'623- add one row to binary tree given val and depth : (REVISIT and REVISE)')    
    print_tree(sol.leet_code_623_add_one_row_to_binary_tree(root, 1, 3))   
    print_tree(sol.leet_code_623_add_one_row_to_binary_tree(root, 2, 2))    
    
    
    values = [1,3,2,5,None,None,9,6,None,7]
    root = build_tree(values)      
    print_tree(root) 
    print(f'662- maximum width of a binary tree (REVISIT and REVISE): {sol.leet_code_662_maximum_width_of_a_binary_tree(root)}')
    values=[1,1,1,1,1,None,1]    
    values=[2,2,2,2,5,2]   
    root = build_tree(values)      
    print_tree(root) 
    print(f'965-uniary-binary-tree:{sol.leet_code_965_univalued_binary_tree(root)}')
    
    
    values = [1,2,3,4]
    x=4
    y=3
    
    values = [1,2,3, None, 4, None, 5]
    x=2
    y=3
    values = [1,2,3,4, None, 5, None, 6]
    x=5
    y=6    
    root = build_tree(values)      
    print_tree(root) 
    print(f'993-cousins in binary tree (REVISIT and REVISE):{sol.leet_code_993_cousins_in_binary_Tree(root, x, y)}')
    
    values = [1,7,0,7, -8, None, None]
    root = build_tree(values)      
    print_tree(root) 
    print(f'1161-maximum level sum:{sol.leet_code_1161_max_level_sum_in_binary_Tree(root)}')

    
    values = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
    print(f'values = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]')
    root = build_nary_tree(values)     
    print_nary_tree(root)
    print(f'429- N-ary-tree-level-order-traversal : {sol.leet_code_429_nary_levelorder_traversal(root)}')
    print(f'515- maximum depth of an N-ary tree : {sol.leet_code_515_max_depth_of_nary_tree(root)}')
