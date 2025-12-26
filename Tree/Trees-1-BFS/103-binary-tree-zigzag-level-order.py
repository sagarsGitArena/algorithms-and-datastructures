from collections import deque


# --------------------------
# TreeNode definition
# --------------------------

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left=left
        self.right=right




def build_tree(values: list):
    

    
    if not list:
        return null
    
    idx = 0
    root = TreeNode(values[idx])

    queue = deque([root])    
    idx += 1
    
    
    while queue and idx < len(values):
        node = queue.popleft()      
        
        
        if values[idx]:
            node.left = TreeNode(values[idx])
            queue.append(node.left)
            idx += 1
        
        if values[idx]:
            node.right = TreeNode(values[idx])
            queue.append(node.right)
            idx += 1
    
        idx += 1
    
    return root
    

# --------------------------
# Print tree sideways
# --------------------------
def print_tree(node: TreeNode | None, prefix: str = "", is_left: bool = True):
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
        

class Solution:
    def zig_zag_level_order_traversal( self, root: TreeNode):
        
        if not TreeNode:
            return []
        
        level_order_zig_zag = []                     
        level_order_zig_zag.append([root.val])
        
        node = root
        queue = deque([root])
        i =0
        
        
        while queue:
            node = queue.popleft()
            children = []
            
            
            if node.left:
                leftNode = node.left
                children.append(leftNode.val)
                queue.append(leftNode)
            
            if node.right:
                rightNode = node.right
                children.append(rightNode.val)
                queue.append(rightNode)
            
            odd_even = i % 2
            
            if len(children) > 0 and odd_even > 0:
                print(f'even-- children: {children} - odd_even:{odd_even}')
                level_order_zig_zag.append(children)
                i += 1
                
            if len(children) > 0 and odd_even == 0:
                print(f'odd-- children: {children} - odd_even:{odd_even}')
                level_order_zig_zag.append(children[::-1])
                i += 1

        return level_order_zig_zag
        
        
        
    def zig_zag_level_order_traversal2( self, root: TreeNode):
        
        if not TreeNode:
            return []
        
        level_order_zig_zag = []        
        
        node = root
        queue = deque([root])
        i =0
        
        
        while queue:
            
            level_zig_zag = []
            
            for _ in range(len(queue)):                
                node = queue.popleft()
                level_zig_zag.append(node.val)
            
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            odd_even = i % 2
            
            if len(level_zig_zag) > 0 and odd_even == 0:
                print(f'even-- children: {level_zig_zag} - odd_even:{odd_even}')
                level_order_zig_zag.append(level_zig_zag)
                
            if len(level_zig_zag) > 0 and odd_even > 0:
                print(f'odd-- children: {level_zig_zag} - odd_even:{odd_even}')
                level_order_zig_zag.append(level_zig_zag[::-1])
                
            i+=1
                

        return level_order_zig_zag

if __name__ == "__main__":
    values = [3,9, 20,None, None, 15, 7]
    
    # for i in values:
    #     print(i)

    root = build_tree(values)      
    print_tree(root)       
    
    
    sol = Solution()
    zig_zag_level_order1 = sol.zig_zag_level_order_traversal(root)
    
    print(zig_zag_level_order1)
    
    
    zig_zag_level_order2 = sol.zig_zag_level_order_traversal2(root)
    
    print(zig_zag_level_order2)
            