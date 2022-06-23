# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def is_univalue_list(head):
  univalue = True # let's assume this is a univalue list

  current = head
  next = current.next
  while next is not None:
    if current.val != next.val:
      univalue = False
    current = next
    next = current.next
  return univalue