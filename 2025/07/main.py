
with open("input.txt") as file:
    grid = [line.rstrip('\n') for line in file]


# Tuple list of active beams
start_col = grid[0].index('S')
beams = [(0, start_col)]
visited = set()
visited.add((0, start_col))

count = 0

while True:
    height = len(grid)
    width = len(grid[0])

    row, col = beams.pop(0)

    next_row = row + 1
    if next_row >= height:
        break
    
    next = grid[next_row][col]
    
    if next == ".":
        if (next_row, col) not in visited:
            visited.add((next_row, col))
            beams.append((next_row, col))
    
    elif next == "^":
        count += 1
        
        # Left beam
        left_col = col - 1
        if 0 <= left_col < width and (next_row, left_col) not in visited:
            visited.add((next_row, left_col))
            beams.append((next_row, left_col))
        
        # Right beam  
        right_col = col + 1
        if 0 <= right_col < width and (next_row, right_col) not in visited:
            visited.add((next_row, right_col))
            beams.append((next_row, right_col))

print(count)




ways = [[0] * width for _ in range(height)]
ways[0][start_col] = 1

for row in range(height - 1):
    for col in range(width):
        w = ways[row][col]
        if w == 0:
            continue

        cell = grid[row + 1][col]
        if cell == '.':
            ways[row + 1][col] += w
        elif cell == '^':
            if col - 1 >= 0:
                ways[row + 1][col - 1] += w
            if col + 1 < width:
                ways[row + 1][col + 1] += w


count = sum(ways[-1])
print(count)



