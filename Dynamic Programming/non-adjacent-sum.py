def non_adjacent_sum(nums):
  return _non_adjacent_sum(nums,0,{}) 

def _non_adjacent_sum(nums, start, memo):
  if start in memo:
    return memo[start]
  # start is where we want to start considering entries in list
  if start >= len(nums):
    return 0
  # binary decision process (I can include a number from sum or exclude)
  include = nums[start] + _non_adjacent_sum(nums, start + 2, memo)
  exclude = _non_adjacent_sum(nums, start + 1, memo)
  memo[start] = max(include, exclude)
  return memo[start]


#test_00:
nums = [2, 4, 5, 12, 7]
print(non_adjacent_sum(nums)) # -> 16

#test_01:
nums = [7, 5, 5, 12]
print(non_adjacent_sum(nums)) # -> 19

#test_02:
nums = [7, 5, 5, 12, 17, 29]
print(non_adjacent_sum(nums)) # -> 48

#test_03:
nums = [
  72, 62, 10,  6, 20, 19, 42,
  46, 24, 78, 30, 41, 75, 38,
  23, 28, 66, 55, 12, 17, 9,
  12, 3, 1, 19, 30, 50, 20
]
print(non_adjacent_sum(nums)) # -> 488

#test_04:
nums = [
  72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
  30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
  83, 80, 56, 68,  6, 22, 56, 96, 77, 98,
  61, 20,  0, 76, 53, 74,  8, 22, 92, 37,
  30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
  72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
  42
]
print(non_adjacent_sum(nums)) # -> 1465