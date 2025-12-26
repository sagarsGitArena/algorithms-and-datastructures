
from collections import deque

class NaryTreeNode:
    def __init__(self, val: int = 0, children: list["NaryTreeNode"] | None = None):
        self.val = val
        # Use empty list if children not provided
        self.children = children if children is not None else []

    def __repr__(self):
        return f"NaryTreeNode({self.val})"
    
#  values = [1, None, 3, 2, 4, None, 5,6]
##This is a working example
def build_nary_tree2(values):
    if not values:
        return None
    
    # First value is the root
    root = NaryTreeNode(values[0])
    queue = deque([root])
    i = 1

    # BFS build
    while queue and i < len(values):
        parent = queue.popleft()
        print(f'parent : { parent}')
        
        if values[i] is None:
            i += 1


        # Add children until we hit None
        while i < len(values) and values[i] is not None:
            child = NaryTreeNode(values[i])
            parent.children.append(child)
            queue.append(child)
            i += 1
            print(f'children :{parent.children}')


    return root



def print_nary_tree(root, level=0):
    if not root:
        return
    print("  " * level + f"- {root.val}")
    for child in root.children:
        print_nary_tree(child, level + 1)


    

class Solution:   
# --------------------------
# Level Order Traversal or BFS
# --------------------------
    def levelOrder(self, root: NaryTreeNode | None) -> list[list[int]]:
        if not root:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                
                # for child in range(len(node.children)):
                #     queue.append(node.children[child])
                for child in node.children:
                    queue.append(child)
    
            result.append(level)
        
        return result    

## driver code

if __name__ == "__main__":
    values = [1, None, 3, 2, 4, None, 5,6]
   #
    values = [1,None,2,3,4,5,None,None,6,7,None,8,None,9,10,None,None,11,None,12,None,13,None,None,14]
  
    root = build_nary_tree2(values)     
    #print("Root:", root)
   
    print_nary_tree(root)
    
    sol = Solution()
    output = sol.levelOrder(root)
    print(" Level Order Traversal:", output)
