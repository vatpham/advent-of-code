
with open("input.txt", "r") as file:
    lines = file.readlines()
    data = [list(map(int, line.split())) for line in lines[:-1]]
    ops = lines[-1].split()


total = 0

for index in range(len(data[0])):
    numbers = [data[row][index] for row in range(len(data))]
    op = ops[index]

    result = numbers[0]
    for number in numbers[1:]:
        if op == "+":
            result += number
        elif op == "*":
            result *= number

    total += result

print(total)

