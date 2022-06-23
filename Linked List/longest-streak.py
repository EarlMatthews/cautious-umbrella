# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def longest_streak(head):

  if head is None:
    return 0
  
  current = head
  prev_val = current.val
  current_streak = 1
  max_streak = 1
  current = current.next
  
  while current:
    if current.val == prev_val:
      current_streak += 1
      if current_streak > max_streak:
        max_streak += 1
    else:
      prev_val = current.val
      current_streak = 1
    current = current.next
  return max_streak