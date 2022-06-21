class Node:
    '''
    Binary tree code
    '''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def all_tree_paths(root):
  # define base case(s)
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [[root.val]]
    paths = []

    left_sub_paths = all_tree_paths(root.left)
    for sub_path in left_sub_paths:
        paths.append([root.val, *sub_path])
    
    right_sub_paths = all_tree_paths(root.right)
    for sub_path in right_sub_paths:
        paths.append([root.val, *sub_path])

    return paths

print(all_tree_paths(a))