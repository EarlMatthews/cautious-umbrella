def count_paths(grid):
    '''
    Write a function, count_paths, that takes in a grid as an argument. 
    In the grid, 'X' represents walls and 'O' represents open spaces. 
    You may only move down or to the right and cannot pass through walls. 
    The function should return the number of ways possible to travel 
    from the top-left corner of the grid to the bottom-right corner.
    '''
    return _count_paths(grid, 0, 0,{})

def _count_paths(grid, r, c, memo):
    # base cases
    if r == len(grid) or c == len(grid[0]): # are we ouside of the grid? If so return 0
        return 0
    
    if grid[r][c] == 'X': # Have we hit a wall? return 0
        return 0
    
    if r == len(grid) - 1 and c == len(grid[0]) -1: # bottom right corner
        return 1 # you're there
    
    if (r,c) in memo:   # Have we seen this position before? If so return that instead of recursive call
        return memo[(r,c)]
    
    down_count = _count_paths(grid, r + 1, c, memo) # down
    right_count= _count_paths(grid, r, c + 1, memo) # move right
    memo[(r,c)] = down_count + right_count
    return down_count + right_count
  
##test_00:
grid = [
  ["O", "O"],
  ["O", "O"],
]
print(count_paths(grid)) # -> 2

##test_01:
grid = [
  ["O", "O", "X"],
  ["O", "O", "O"],
  ["O", "O", "O"],
]

print(count_paths(grid))

#test_02:
grid = [
  ["O", "O", "O"],
  ["O", "O", "X"],
  ["O", "O", "O"],
]
print(count_paths(grid)) # -> 3
#test_03:
grid = [
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["O", "O", "O"],
]

print(count_paths(grid)) # -> 1

#test_04:
grid = [
  ["O", "O", "X", "O", "O", "O"],
  ["O", "O", "X", "O", "O", "O"],
  ["X", "O", "X", "O", "O", "O"],
  ["X", "X", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O"],
]
print(count_paths(grid)) # -> 0

#test_05:
grid = [
  ["O", "O", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "X"],
  ["X", "O", "O", "O", "O", "O"],
  ["X", "X", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O"],
]
print(count_paths(grid)) # -> 42

#test_06:
grid = [
  ["O", "O", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "X"],
  ["X", "O", "O", "O", "O", "O"],
  ["X", "X", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "X"],
]
print(count_paths(grid)) # -> 0

#test_07:
grid = [
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
]
print(count_paths(grid)) # -> 40116600
#test_08:
grid = [
  ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
  ["X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
  ["X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "X", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
  ["X", "X", "X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
]
print(count_paths(grid)) # -> 3190434