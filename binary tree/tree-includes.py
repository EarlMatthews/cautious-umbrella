# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
    '''
    Write a function, tree_includes, that takes in the root of a binary tree and a target value.
     The function should return a boolean indicating whether or not the value is contained in the tree.
    '''
    if root is None:
        return False
    if  (root.val == target) or\
        (tree_includes(root.left,target)) or\
        (tree_includes(root.right,target)):
        return True
    else:
        return False
