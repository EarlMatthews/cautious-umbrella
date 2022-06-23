# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def reverse_list(head):
#   current = head
#   prev = None
#   while current is not None:
#     next = current.next
#     current.next = prev
#     prev = current
#     current = next
#   return prev
    
def reverse_list(head,prev=None):
  ''' recursive '''
  if head is None:
    return prev
  next = head.next
  head.next = prev
  return reverse_list(next, head)
