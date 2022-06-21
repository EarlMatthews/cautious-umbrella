from collections import deque


class Node:
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


def tree_levels_stack(root):
    '''
        DOC_STRING
    '''
    if root is None:
        return []
    stack = [(root, 0)]  # stack will hold node value and level
    levels = []  # tree_levels return value

    while stack:
        node, level_num = stack.pop()  # (node_value, level)

        if len(levels) == level_num:
            levels.append([node.val])
        else:
            levels[level_num].append(node.val)

        if node.right is not None:
            stack.append((node.right, level_num + 1))
        if node.left is not None:
            stack.append((node.left, level_num + 1))

    return levels


def tree_levels(root):
    '''
    DOC_STRING:
    '''
    if root is None:
        return []
    queue = deque([(root, 0)])  # queue will hold node value and level
    levels = []  # tree_levels return value

    while queue:
        node, level_num = queue.popleft()  # (node_value, level)

        if len(levels) == level_num:
            levels.append([node.val])
        else:
            levels[level_num].append(node.val)

        if node.left is not None:
            queue.append((node.left, level_num + 1))

        if node.right is not None:
            queue.append((node.right, level_num + 1))

    return levels


print(tree_levels(a))
print(tree_levels_stack(a))
