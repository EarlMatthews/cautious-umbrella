def count_paths(grid):
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
  
  
grid = [
  ["O", "O", "X"],
  ["O", "O", "O"],
  ["O", "O", "O"],
]

print(count_paths(grid))