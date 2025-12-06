
with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

total = 0

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]

for row in range(len(grid)):
    for col in range(len(grid[row])):
        count = 0   
        if grid[row][col] == "@":
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[row]):
                    if grid[r][c] == "@":
                        count += 1
            if count < 4:
                total += 1

print(total)


total = 0

while True:
    to_remove = []

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            count = 0   
            if grid[row][col] == "@":
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if 0 <= r < len(grid) and 0 <= c < len(grid[row]):
                        if grid[r][c] == "@":
                            count += 1
                if count < 4:
                    to_remove.append((row, col))
    
    if not to_remove:
        break

    for row, col in to_remove:
        grid[row][col] = "."
        total += 1

print(total)

