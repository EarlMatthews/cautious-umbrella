# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque
def bottom_right_value(root):
    '''
    test
    '''
    queue = deque([ root ])

    while queue:
        current = queue.pop()
        if current.left:
            queue.appendleft(current.left)
        if current.right:
            queue.appendleft(current.right)
    return current.val