# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# def linked_list_cycle(head):
#   if not head:
#     return False
#   seen = set() # set to track items we've seen
#   current = head
	
#   # loop until we've either seen a duplicate or find the tail
#   while current:
#     if current not in seen:
#       seen.add(current)
#     else:
#       return True
		
#     if current.next is None:
#       return False
#     #remember to move the pointer to the next item in loop
#     current = current.next
		
def linked_list_cycle(head):
	slow = head
	fast = head
	first_iteration = True
	
	while not (fast is None or fast.next is None):
		if slow is fast and not first_iteration:
			return True
		slow = slow.next
		fast = fast.next.next
		first_iteration = False
	return False
