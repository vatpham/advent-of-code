
ranges = []
ingredients = []

with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        if "-" in line:
            ranges.append(line)
        elif line:
            ingredients.append(line)

count = 0

for ingredient in ingredients:
    for range in ranges:
        start, end = map(int, range.split('-'))
        start, end, ingredient = int(start), int(end), int(ingredient)
        if start <= ingredient <= end:
            count += 1
            break

print(count)


merged = []
ranges = [(int(start), int(end)) for start, end in (range.split("-") for range in ranges)]
ranges.sort()

for start, end in ranges:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

count = sum(end - start + 1 for start, end in merged)

print(count)

