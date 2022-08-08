'''
max increasing subseq
Write a function, max_increasing_subseq, that takes in a list of numbers as an argument. The function should return the length of the longest subsequence of strictly increasing numbers.

A subsequence of a list can be created by deleting any items of the list, while maintaining the relative order of items.

'''


def max_increasing_subseq(numbers):
  return _max_increasing_subseq(numbers, 0, float('-inf'), {})

def _max_increasing_subseq(numbers, i, previous, memo):
  key = (i, previous)
  if key in memo:
    return memo[key]
  
  if i == len(numbers):
    return 0
  
  current = numbers[i]
  options = []
  dont_take_current = _max_increasing_subseq(numbers, i + 1, previous, memo)
  options.append(dont_take_current)
  
  if current > previous:
    take_current = 1 + _max_increasing_subseq(numbers, i+1, current, memo)
    options.append(take_current)
  
  memo[key] = max(options)
  return memo[key]


'''test_00:'''
numbers = [4, 18, 20, 10, 12, 15, 19]
print(max_increasing_subseq(numbers)) # -> 5

'''test_01:'''
numbers = [12, 9, 2, 5, 4, 32, 90, 20]
print(max_increasing_subseq(numbers)) # -> 4

'''test_02:'''
numbers = [42, 50, 51, 60, 55, 70, 4, 5, 70]
print(max_increasing_subseq(numbers)) # -> 5

'''test_03:'''
numbers = [7, 14, 10, 12]
print(max_increasing_subseq(numbers)) # -> 3

'''test_04:'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
print(max_increasing_subseq(numbers)) # -> 21

'''test_05:'''
numbers = [
  1, 2, 3, 4, 5, 12, 6, 30, 7, 8, 9, 10, 11, 12, 13, 10, 18, 14, 15, 16, 17, 18, 19, 20, 21, 100,
  104,
]
print(max_increasing_subseq(numbers)) # -> 23

'''test_06:'''
numbers = [
  1, 2, 300, 3, 4, 305, 5, 12, 6, 30, 7, 8, 9, 10, 10, 10, 15, 11, 12, 13, 10, 18, 14, 15, 16,
  17, 18, 19, 20, 21, 100,101 ,102, 103, 104, 105
]
print(max_increasing_subseq(numbers)) # -> 27