# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def linked_list_find(head, target):
#   current = head
#   while current:
#     if current.val == target:
#       return True
#     current = current.next
#   return False

def linked_list_find(head,target):
  if head is None: 
    return False
  return (head.val == target) or linked_list_find(head.next, target)
