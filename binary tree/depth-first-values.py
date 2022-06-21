class Node:
    '''
    Sample Node
    '''
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Sample data
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

#def depth_first_values(root):
#   if root is None: #check if root is None because [None] is a valid list
#     return []
  
#   stack = [ root ]
#   values = []
  
#   while stack:
#     current = stack.pop()
#     values.append(current.val)
#     if current.right:
#       stack.append(current.right)
#     if current.left:
#       stack.append(current.left)
#   return values

def depth_first_values(root):
    '''
        DOC_STRING
        Write a function, depth_first_values, that takes in the root of a binary tree. The function should return a list containing all values of the tree in depth-first order.
        Hey. This is our first binary tree problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ
    '''
    if root is None:
        return []
    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)
    return [root.val, *left_values, *right_values]

print(depth_first_values(a))