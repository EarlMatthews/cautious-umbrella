def island_count(grid):
    '''
    Write a function, island_count, that takes in a grid containing Ws and Ls.
    W represents water and L represents land.
    The function should return the number of islands on the grid.
    An island is a vertically or horizontally connected region of land.
    '''
    visited = set([])
    count = 0
    #iterate through every row, col position
    for r in range(len(grid)):
        for c in range(len(grid[0])): # grid may not be square
            if explore(grid, r, c, visited) == True:
                count += 1
    return count

def explore(grid, r, c, visited):
    # return True or False depending on if it traversed a new island
    row_inbounds = 0 <= r < len(grid)   # make sure r is less than len(grid) *NOT* less than or equal
    col_inbounds = 0 <= c < len(grid[0])
    # check if r and c are valid locations on the grid
    if not row_inbounds or not col_inbounds:
        return False
    # check if the node is water
    if grid[r][c] == "W":
        return False
    # everything from here is inbounds and land
    pos = (r,c)
    if pos in visited:
        return False
    visited.add(pos)
  
    explore(grid, r - 1, c, visited)  #up
    explore(grid, r + 1, c, visited)  #down
    explore(grid, r, c - 1, visited)  #left
    explore(grid, r, c + 1, visited)  #right
    return True # done exploring

# test 00:

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid)) # -> 3

#test 01:
grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(island_count(grid)) # -> 4

# test 02:
grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

print(island_count(grid)) # -> 1

#test 04:
grid = [
  ['W', 'W'],
  ['W', 'W'],
  ['W', 'W'],
]

print(island_count(grid)) # -> 0