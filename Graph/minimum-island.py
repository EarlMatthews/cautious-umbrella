def minimum_island(grid):
    visited = set()
    min_size = float('inf')
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore_size(grid,r,c,visited)
            if size > 0 and size < min_size:
                min_size = size
    return min_size

def explore_size(grid, r, c, visited):
    # return the size of the island visited
    #check if r and c are inbounds
    row_inbounds = 0 <= r < len(grid)
    col_inbounds = 0 <= c < len(grid[0])
    # check if r and c are valid locations on the grid
    if not row_inbounds or not col_inbounds:
        return 0
    # check if we are looking at water
    if grid[r][c] == 'W':
        return 0
    #check if we have visited this position before
    pos = (r,c)
    if pos in visited:
        return 0
    visited.add(pos)
    size = 1 # count node
    # add up the sizes from the recursive calls
    size += explore_size(grid, r - 1, c, visited)  #up
    size += explore_size(grid, r + 1, c, visited)  #down
    size += explore_size(grid, r, c - 1, visited)  #left
    size += explore_size(grid, r, c + 1, visited)  #right

    return size

#test_00:
grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(grid)) # -> 2
#test_01:
grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(minimum_island(grid)) # -> 1
#test_02:
grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

print(minimum_island(grid)) # -> 9
#test_03:
grid = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]

print(minimum_island(grid)) # -> 1