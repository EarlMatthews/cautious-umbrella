from collections import deque

def breadth_first_values(root):
    '''
    Write a function, breadth_first_values, that takes in the root of a binary tree.
    The function should return a list containing all values of the tree in breadth-first order.
    '''
    if root is None:
        return []
    queue = deque([ root ])
    values = []
    while queue:
        current = queue.popleft()
        values.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return values
