# def intersection(a, b):
#   s_a, s_b = set(a), set(b)
#   return list(s_a.intersection(s_b))

def intersection(a,b):
  set_a = set(a)
  return [ele for ele in b if ele in set_a]

# def intersection(a,b):
#   result = []
#   for item in a:
#     if item in b:
#       result.append(item)
#   return result
# def intersection(a,b):
#   '''
#   TOO SLOW
#   '''
#   result = []
#   for i in a:
#     for j in b:
#       if i == j:
#         result.append(i)
#   return result

a = [4,2,1,6]
b = [3,6,9,2,10]
print (intersection(a,b))