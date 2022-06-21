class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# def tree_sum(root):
#   if root is None:
#     return 0
#   stack = [root]
#   sum = 0
#   while stack:
#     current = stack.pop()
#     sum += current.val
#     if current.right:
#       stack.append(current.right)
#     if current.left:
#       stack.append(current.left)
#   return sum

def tree_sum(root):
    '''
    Write a function, tree_sum, that takes in the root of a binary tree that contains number values. The function should return the total sum of all values in the tree.
    '''
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)
