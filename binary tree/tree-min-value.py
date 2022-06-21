# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
    '''
    Write a function, tree_min_value, 
    that takes in the root of a binary tree that contains number values.
     The function should return the minimum value within the tree.
    You may assume that the input tree is non-empty.
    '''
    if root is None:
        return float("inf")
    return min(root.val,tree_min_value(root.left),
            tree_min_value(root.right))