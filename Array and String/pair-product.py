# def pair_product(numbers, target_product):
'''
Loop through list using i as an index
for each i loop from i+1 to end of list (j)
mulitply numbers[i] * numbers[j] if they equal target_product
return the indicies (i,j) as a tuple
'''
#   for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#       if numbers[i] * numbers[j] == target_product:
#         return (i,j)
def pair_product(numbers, target_product):
  '''
  set up a dictionary to hold previously seen numbers
  iterate through the list generating the complement (target/num)
  then looking for it in the dictionary
  if the complement is found in the dictionary return it and the current
  index
  either way place the number as they are seen into the dictionary
  '''
  previous_num = {}  #dictionary of previous seen numbers
  for index,num in enumerate(numbers):
    complement = target_product / num
    
    if complement in previous_num:
      return (previous_num[complement],index)
    
    previous_num[num] = index