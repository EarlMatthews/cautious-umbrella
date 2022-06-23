class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_list(head):
    if head is None:
        return
    print(head.val)
    print_list(head.next)