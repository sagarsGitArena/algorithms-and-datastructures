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
        print(f'idx : {i} -- value {node.val}')
       
        
        if  i < len(values) and values[i]:
            node.left = BinaryTreeNode(values[i])
            queue.append(node.left)

        i +=1 
        
        if  i < len(values) and values[i]:
            node.right = BinaryTreeNode(values[i])
            queue.append(node.right)
        
        i += 1
    
    return root

def build_tree_level_order(arr):
    if not arr or arr[0] is None:
        return None
    
    root = BinaryTreeNode(arr[0])
    queue = [root]
    i = 1
    
    while queue and i < len(arr):
        current = queue.pop(0)  # deque would be faster
        
        # Left child
        if i < len(arr) and arr[i] is not None:
            current.left = BinaryTreeNode(arr[i])
            queue.append(current.left)
        i += 1
        
        # Right child
        if i < len(arr) and arr[i] is not None:
            current.right = BinaryTreeNode(arr[i])
            queue.append(current.right)
        i += 1
            
    return root


def build_tree3(values):
    if not values or values[0] is None:
        return None

    root = BinaryTreeNode(values[0])
    queue = deque([root])
    i = 1

    print(f"Root created: {root.val}")

    while queue and i < len(values):
        parent = queue.popleft()
        print(f"\nPARENT POPPED: {parent.val}")

        # LEFT CHILD
        if i < len(values):
            print(f"  Left value at index {i}: {values[i]}")
            if values[i] is not None:
                parent.left = BinaryTreeNode(values[i])
                queue.append(parent.left)
                print(f"    → Created LEFT child {values[i]} under {parent.val}")
            i += 1

        # RIGHT CHILD
        if i < len(values):
            print(f"  Right value at index {i}: {values[i]}")
            if values[i] is not None:
                parent.right = BinaryTreeNode(values[i])
                queue.append(parent.right)
                print(f"    → Created RIGHT child {values[i]} under {parent.val}")
            i += 1

    return root


def build_tree_indexed(values, i=0):
    if i >= len(values) or values[i] is None:
        return None

    node = BinaryTreeNode(values[i])
    node.left = build_tree_indexed(values, 2*i + 1)
    node.right = build_tree_indexed(values, 2*i + 2)
    return node

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

## driver code

if __name__ == "__main__":
    values = [3,9, 20,None, None, 15, 7]
    values = [3, None, 20, None, None, 16, 7]
    
  
       
    #root = build_tree_indexed(values)  
    root = build_tree_level_order(values)
    print_tree(root) 