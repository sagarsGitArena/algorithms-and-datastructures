

# from typing import Optional, List
from collections import deque


# --------------------------
# TreeNode definition
# --------------------------

class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None, next = None):
        self.val = val
        self.left=left
        self.right=right
        self.next=next



def print_levels_with_next(root):
    level_start = root

    while level_start:
        curr = level_start
        level_str = []

        # walk horizontally using `.next`
        while curr:
            nxt = curr.next.val if curr.next else None
            level_str.append(f"{curr.val} -> {nxt}")
            curr = curr.next

        print("   ".join(level_str))

        # move down: for perfect tree we can just use left child
        # for LC117 (general), we should find the first child
        if level_start.left:
            level_start = level_start.left
        elif level_start.right:
            level_start = level_start.right
        else:
            # find first child in level linked by next pointers
            tmp = level_start.next
            found = None
            while tmp and not found:
                if tmp.left:
                    found = tmp.left
                elif tmp.right:
                    found = tmp.right
                tmp = tmp.next
            level_start = found


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
    
    
    def leet_code_104_maximum_depth_of_bst(self, root: BinaryTreeNode):
        
        max_depth = 0
        
        
        def helper(node : BinaryTreeNode, level :int):
            nonlocal max_depth
            
            if not node:
                return 0
            
            level += 1
            if not node.left and not node.right:
                max_depth = max(max_depth, level)
            
            if node.left:
                helper(node.left, level)
            
            if node.right:
                helper(node.right, level)


    
        helper(root, 0)      
        return max_depth


    def leet_code_103_minimum_depth_of_bst(self, root: BinaryTreeNode):
        min_depth = float("inf")
        
        def helper(node: BinaryTreeNode, level :int ):
            nonlocal min_depth
            if not node:
                return 0
            
            level += 1
            if not node.left and not node.right:                
                min_depth = min(min_depth, level)
                
            if node.left:
                helper(node.left, level)
            if node.right:
                helper(node.right, level)
        
        helper(root, 0)
        return min_depth
    
    def leet_code_112_path_sum_i(self, root: BinaryTreeNode, targetSum : int):
        
        result = False
        
        def helper(node: BinaryTreeNode, target_sum:int, sum: int):
            nonlocal result
            
            if not node:
                return
            
            
            sum += node.val
            print(f'node.val:{node.val} -- SUM:{sum}')
            if not node.left and not node.right:
                if sum == target_sum:
                    result = True
            
            if node.left:
                helper(node.left, target_sum, sum)
            
            if node.right:
                helper(node.right, target_sum, sum)
        
        helper(root, targetSum, 0)
        return result

    def leet_code_113_path_sum_ii(self, node : BinaryTreeNode, target_sum: int):
        
        result = []
        
        def helper(node: BinaryTreeNode, target_sum, sum: int, path: list):
            if not node:
                return []
            
            
            sum += node.val
            path.append(node.val)
            print(f'node.val:{node.val} -- SUM:{sum} - {path}')
            if not node.left and not node.right:
                if sum == target_sum:                
                    result.append(path.copy())
            
            if node.left:
                helper(node.left, target_sum, sum, path)
            
            if node.right:
                helper(node.right, target_sum, sum, path)
            
            path.pop()
        
        helper(root, targetSum, 0, [])
        return result
        
    def leet_code_116_populate_next_right_pointer_in_each_node_of_a_perfect_binary_tree(self, root : BinaryTreeNode):
        
        def helper(node :BinaryTreeNode, right_node : BinaryTreeNode):
            
            if not node:
                return 
            
            node.next = right_node
            
            if node.left:
                helper(node.left, node.right)
                
            if node.right:
                if right_node:
                    helper(node.right, right_node.left)
                else:
                    helper(node.right, None)
        
        helper(root, None)
        return root

    def leet_code_116_populate_next_right_pointer_in_each_node_of_a_perfect_binary_tree2(self, root : BinaryTreeNode):
        
        def helper(node: BinaryTreeNode):
            if not node:
                return None
            
            if node.left:
                node.left.next = node.right
            
            if node.next and node.right:
                node.right.next = node.next.left
            
            helper(node.left)
            helper(node.right)
        
        helper(root)
        
        return root
    
    
    
    def leet_code_117_populate_next_right_pointer_in_each_node_of_an_imperfect_binary_tree(self, root: BinaryTreeNode):
        def find_next_node(node: BinaryTreeNode):
            while node:
                if node.left:
                    return node.left
                if node.right:
                    return node.right
                
                node = node.next


            return node
        
        def helper(node: BinaryTreeNode):
            if not node:
                return None
            
            next_node = find_next_node(node.next)

            
            if node.right:
                node.right.next = next_node
            
            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    node.left.next = next_node\
            
            
            
            helper(node.left)
            helper(node.right)
            
        
        helper(root)
        return root
    
    def leetcode_226_invert_a_binary_tree(self, root: BinaryTreeNode):
        
        def helper(node: BinaryTreeNode):
            if not node:
                return None
        
            tmp = node.left
            node.left = node.right
            node.right = tmp
            ## instead you can do the following to swap
            #node.left, node.right = node.right, node.left

            
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return root

    def leetcode_257_binary_tree_path(self, root: BinaryTreeNode):
        result = []
        
        def helper(node: BinaryTreeNode, slate: list):
            if not node:
                return None
            
            slate.append(node.val)
            if not node.left and not node.right:
                #result.append(slate[:])
                result.append("->".join(map(str, slate)))
            else:
                helper(node.left, slate)
                helper(node.right, slate)
            slate.pop()
            
        
        helper(root, [])        
        return result

    def leet_code_298_binary_tree_longest_consecutive_sequence(self, root: BinaryTreeNode):
        
        global_max = 1
        
        
        def helper2(node: BinaryTreeNode, parent_node_val: int, seq_cnt: int):
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
    
    def leet_code_298_binary_tree_longest_consecutive_sequence_2(self, root: BinaryTreeNode):
        if not root:
            return []
        
        global_result = []
        
        ## The following is rebinding solution. Also compare with other version of the soution where we dont pop at all. 
        def helper(node: BinaryTreeNode, parent_val:int, result):
            nonlocal  global_result
            if not node:
                return
            
            if node.val -1 == parent_val:
                result.append(node.val)
            else:
                ## This mutates and not recommended, as you cannot backtrack
                #result.clear()
                #result.append(node.val)
                ##The following just rebinds and not mutates. Helps backtracking. We need to ensure we only backtrack the last element added(appended)
                result = [node.val]
                
            if len(result) > len(global_result):                
                global_result = result[:]
            

            
            helper(node.left, node.val, result)
            helper(node.right, node.val, result)

            # Only backtrack if we mutated the same list (appended)
            if  result and result[-1] == node.val and node.val == parent_val + 1:
                result.pop()
            
        
        helper(root, root.val - 1, [])
        return global_result
    
    
    ### Rebinding copy on write solution
    def leet_code_298_binary_tree_longest_consecutive_sequence_2_v2(self, root: BinaryTreeNode):
        if not root:
            return []
        
        global_result = []
        
        ## The following is rebinding solution. Also compare with other version of the soution where we dont pop at all. 
        def helper(node: BinaryTreeNode, parent_val:int, result):
            nonlocal  global_result
            if not node:
                return
            
            ## Here we are creating new list every time: Rebinding/copy on write
            if node.val == parent_val + 1:
                new_result = result + [node.val] 
            else:
                new_result = [node.val]

            if len(new_result) > len(global_result):
                global_result = new_result
            
            
            helper(node.left, node.val, new_result)
            helper(node.right, node.val, new_result)
            ## HEre you dont need to pop as we every time have new list at each branch.
        
        helper(root, root.val - 1, [])
        return global_result
            
        
if __name__ == "__main__":
    values = [3,9,20,None,None,15,7]
    
    
    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    print(f'104 maximum depth of a bianry tree : {sol.leet_code_104_maximum_depth_of_bst(root)}')
    print(f'103 minimum depth of a bianry tree : {sol.leet_code_103_minimum_depth_of_bst(root)}')    
    
    values = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    targetSum = 22
    root = build_tree(values)      
    print_tree(root)    
    
    print(f'112 path sum i : {sol.leet_code_112_path_sum_i(root, targetSum )}')
    print(f'113 path sum ii: {sol.leet_code_113_path_sum_ii(root, targetSum)}')
    
    values  = [1,2,3,4,5,6,7]
    root = build_tree(values)      
    print_tree(root)    
    print(f'116 populate next right pointer in each node of perfect binary tree v1(REVISE AND REVISIT): ')
    modified_tree = sol.leet_code_116_populate_next_right_pointer_in_each_node_of_a_perfect_binary_tree(root)
    print_levels_with_next(modified_tree)
    
    
    values  = [1,2,3,4,5,6,7]
    root = build_tree(values)      
    print_tree(root)    
    print(f'116 populate next right pointer in each node of perfect binary tree v2(REVISE AND REVISIT): ')
    modified_tree2 = sol.leet_code_116_populate_next_right_pointer_in_each_node_of_a_perfect_binary_tree2(root)
    print_levels_with_next(modified_tree2)
    
    values  = [1,2,3,4,5,None,7]
    values = [1,2,3,4, None,None, 7]
    values = [1,2,3,4, None,None, 5,6,None, 7, 8,9,None,None,None,None,10]
    root = build_tree(values)      
    print_tree(root)    
    print(f'117 populate next right pointer in each node of imperfect binary tree v1(REVISE AND REVISIT): ')
    modified_tree = sol.leet_code_117_populate_next_right_pointer_in_each_node_of_an_imperfect_binary_tree(root)
    print_levels_with_next(modified_tree)
    
    values = [4,2,7,1,3,6,9]
    root = build_tree(values)      
    print_tree(root)    
    print(f'226 Invert a binary tree: ')
    modified_tree = sol.leetcode_226_invert_a_binary_tree(root)
    print_tree(modified_tree) 
    
    values = [1,2,3,4, None,None, 5,6,None, 7, 8,9,None,None,None,None,10]
    root = build_tree(values)      
    print_tree(root)    
    print(f'257 binary_tree_path: ')
    print(sol.leetcode_257_binary_tree_path(root))
    


    print(f'298 binary tree longest consequence sequence: (REVISIT THIS AGAIN) ')  
    values = [1,None,3,2,4,None,None,None,5]
    #values = [2,None,3,2,None,1]
    #values = [2,None,3,2,1,4]
    values = [1,None,3,2,4,3, 4, None ,5,8,4, None,None,None, None, None, None, 5, None]
    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()  
    print(sol.leet_code_298_binary_tree_longest_consecutive_sequence(root))



    print(f'298 binary tree longest consequence sequence: (REVISIT THIS AGAIN) ')  
    values = [1,None,3,2,4,None,None,None,5]
    #values = [2,None,3,2,None,1]
    #values = [2,None,3,2,1,4]
    values = [1,None,3,2,4,3, 4, None ,5,8,4, None,None,None, None, None, None, 5, None]
    root = build_tree(values)      
    print_tree(root)  
    sol = Solution()  
    print(sol.leet_code_298_binary_tree_longest_consecutive_sequence_2(root))
    
    print(f'298 binary tree longest consequence sequence _V2: (REVISIT THIS AGAIN) ')  
    values = [1,None,3,2,4,None,None,None,5]
    #values = [2,None,3,2,None,1]
    #values = [2,None,3,2,1,4]
    values = [1,None,3,2,4,3, 4, None ,5,8,4, None,None,None, None, None, None, 5, None]
    root = build_tree(values)      
    print_tree(root)  
    sol = Solution()  
    print(sol.leet_code_298_binary_tree_longest_consecutive_sequence_2_v2(root))