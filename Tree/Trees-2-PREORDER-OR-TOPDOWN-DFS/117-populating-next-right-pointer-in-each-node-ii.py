from collections import deque


# --------------------------
# TreeNode definition
# --------------------------

class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left=left
        self.right=right
        self.next=next
        
    

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


class Solution:
    def populate_next_bin_tree_in_each_node(self, root :BinaryTreeNode):       
        
        
        def helper(node: BinaryTreeNode, my_next_right: BinaryTreeNode):
            if not node:
                return
            
            node.next = my_next_right
            
            
            target = None
            while my_next_right:
                
                if my_next_right.left:
                    target = my_next_right.left
                    break                
                elif my_next_right.right:
                    target= my_next_right.right
                    break
                my_next_right = my_next_right.next
            
            if node.right:
                helper(node.right, target)
            
            if node.left:
                if node.right:
                    helper(node.left, node.right)
                else:
                    helper(node.left, target)
                
            
        helper(root, None)
        return root
            
        
        
        helper(root, None)
        return root

            

if __name__ == "__main__":
    values = [1,2,3,4,5, None,7,8,None, 10, 11, 12, None, None, 13, None, None, None, None, None, 19]

    root = build_tree(values)      
    print_tree(root)    
    
    sol = Solution()
    root_with_next_ptr = sol.populate_next_bin_tree_in_each_node(root)
    print_levels_with_next(root_with_next_ptr)
    
        