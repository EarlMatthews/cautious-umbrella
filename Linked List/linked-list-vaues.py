# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def linked_list_values(head):
#   r = []
#   current = head
#   while current:
#     r.append(current.val)
#     current = current.next
#   return r

def linked_list_values(head):
  ''' 
  recursive
  '''
  if head is None:
    return []
  else:
    return [head.val, *linked_list_values(head.next)]