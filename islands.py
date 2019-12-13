# Write a function that takes a 2D binary array and
# returns the number of 1 islands. An island consists 
# of 1s that are connected to the north, south, east, or west.
# For Example:

# Undirected, unweighted, cyclic
# Not an adjancency matrix bc each row/column does not represent node/edge
# In matrix here = numbers represent nodes
# Nodes are numbers
# Edges are connections between numbers
# Diagonals don't count

islands =  [[0, 1, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0. 0. 1. 0. 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 0, 0]]

# islands[0] = [0, 1, 0, 1, 0]
# islands[1] = [1, 1, 0, 1, 1]
# islands[2] = [0. 0. 1. 0. 0]
# islands[3] = [1, 0, 1, 0, 0]
# islands[4] = [1, 1, 0, 0, 0]
# island[2][3] = 0

islands[4][2]

islands_counter(islands) # returns 4

# Visit each cell in the 2d array
# When you come across a 1, traverse it and mark all connected nodes as visited
# Then increment a counter



# Plan:
# 1. Is this a graph problem?
#      - If so, translate the problem into graph terminology
# 2. Build the graph
# 3. Traverse the graph


# Lists are not hashable but sets are

def get_island_neighbors(x, y, matrix):
    neighbors = []
    # Check north
    if y > 0 and matrix[y-1][x] == 1:
        neighbors.append( (x, y-1) )
    # Check south
    if y < len(matrix) and matrix[y+1][x] == 1:
        neighbors.append( (x, y+1) )
    # Check east
    if x < len(matrix[0]) and matrix[y][x+1] == 1:
        neighbors.append( (x+1, y) )
    # Check west
    if x > 0 and matrix[y][x-1] == 1:
        neighbors.append( (x-1, y) )
    return neighbors


def dft_islands(start_x, start_y, matrix, visited):
    # Retrurns an updated visited matrix after a DFT of matrix starting from x, y
    s = Stack()
    s.push( (start_x, start_y) )
    while s.size() > 0:
        v = s.pop()
        x = v[0]
        y = v[1]

        if not visited[y][x]:   
            visited[y][x] = True
            for neighbor in get_island_neighbors(x, y, matrix): #STUB
                s.push(neighbor)
    return visited

def island_counter(matrix):
    # Create a visited matrix with the same dimensions as the islands matrix
    visited = []
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    for i in range(matrix_height):
        visited.append( [False] * matrix_width )
    # Create a counter, initialize to 0
    counter = 0
    # For each cell in the 2d array
    for x in range(matrix_width):
        for y in range(matrix_height)
            # If it has not been visited...
            if not visited[y][x]:
                # When you come across a 1
                if matrix[y][x] == 1:
                    # DFT it and mark all connected nodes as visited
                    visited = dft_islands(x, y, matrix_visited) # STUB
                    # Then increment a counter
                    counter+=1
    return counter