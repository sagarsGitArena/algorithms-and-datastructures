
from collections import deque

class NaryTreeNode:
    def __init__(self, val: int = 0, children: list["NaryTreeNode"] | None = None):
        self.val = val
        # Use empty list if children not provided
        self.children = children if children is not None else []

    def __repr__(self):
        return f"NaryTreeNode({self.val})"
    


#  values = [1, None, 3, 2, 4, None, 5,6]
def build_nary_tree(values: list):
    
    root = NaryTreeNode(values[0])
    
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        parent_node = queue.popleft()
        
        if values[i] is None:
            i += 1
        
        children = []
        while i < len(values) and values[i] is not None:
            child = NaryTreeNode(values[i])            
            queue.append(child)
            children.append(child)
            i += 1
            
        parent_node.children = children
        
    
    return root
        
def print_nary_tree(root, level=0):
    if not root:
        return
    print("  " * level + f"- {root.val}")
    for child in root.children:
        print_nary_tree(child, level + 1)
        


class Solution:
    
    def maximum_depth_of_nary_tree(self, root: NaryTreeNode):
        
        if not values:
            return 0
        
        queue = deque([root])
        max_depth = 0
        
        while queue:
            max_depth += 1 
            for _ in range(len(queue)):
                nary_node = queue.popleft()
                children = nary_node.children 
                
                for i in range(len(children)):
                    queue.append(children[i])
            
            
                
        return max_depth
            
            
            
        
        



if __name__ == "__main__":
    values = [1, None, 3, 2, 4, None, 5,6]

   # values = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]

    root = build_nary_tree(values)     
    #print("Root:", root)
    print_nary_tree(root)
    
    sol = Solution()
    max_depth = sol.maximum_depth_of_nary_tree(root)
    
    print(f'max depth of nary tree: {max_depth}')
