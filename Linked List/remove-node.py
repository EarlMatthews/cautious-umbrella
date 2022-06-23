# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def remove_node(head, target_val):
#   if head.val == target_val:
#     return head.next
  
#   current = head.next
#   prev = head

#   while current is not None:
#     if current.val == target_val:
#         prev.next = current.next # reroute link to current.next
#         break # if you've done the deletion leave loop 
#     prev = current
#     current = current.next
#   return head

# def print_list(head):
#     if head is None:
#         return
#     print(head.val)
#     print_list(head.next)

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")

# a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# # a -> b -> c -> d -> e -> f
# print_list(a)
# remove_node(a, "c")
# print("-------------")
# # a -> b -> d -> e -> f
# print_list(a)

def remove_node(head,target_val):
  if head is None:
    return None
  if head.val == target_val:
    return head.next
  head.next = remove_node(head.next,target_val)
  
  return head
