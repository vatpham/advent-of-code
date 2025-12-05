
with open("input.txt", "r") as file:
    rotations = [line.strip() for line in file]

number = 50
count = 0

for rotation in rotations:
    if rotation.startswith("R"):
        number += int(rotation[1:])
        number = number % 100
    else:
        number -= int(rotation[1:])
        number = number % 100
    
    if number == 0:
        count += 1

print(number)
print(count)


number = 50
count = 0

for rotation in rotations:
    steps = int(rotation[1:])
    if rotation.startswith("R"):
        delta = 1
    else:
        delta = -1
    for _ in range(steps):
        number = (number + delta) % 100
        if number == 0:
            count += 1

print(number)
print(count)