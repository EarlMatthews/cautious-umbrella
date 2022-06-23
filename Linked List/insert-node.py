class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def print_list(head):
    if head is None:
        return
    print(f"{head.val} ->", end='')
    print_list(head.next)
    

def insert_node(head, value, index):
  count = 0
  current = head
  if index == 0:
    temp = Node(value)
    temp.next = head
    head = temp
    return head
  while current is not None:
    if count == index - 1:
      #insertion
      temp = current.next
      current.next = Node(value)
      current.next.next = temp
      
    count += 1
    current = current.next
  return head

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

print_list(a)
print()
insert_node(a,'x',0)
print_list(insert_node(a,'x',0))