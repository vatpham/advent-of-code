
with open("input.txt", "r") as file:
    banks = [line.strip() for line in file]

total = 0

for bank in banks:
    first_battery = max(int(battery) for battery in bank[:-1])
    second_battery = max(int(battery) for battery in bank[bank[:-1].index(str(first_battery)) + 1:])
    total += int(str(first_battery)+str(second_battery))
    
print(total)
    


total = 0

for bank in banks:
    batteries = [int(battery) for battery in bank.strip()]
    batteries_left = 12
    discards_left = len(batteries) - batteries_left

    picked_batteries = []

    for battery in batteries:
        while picked_batteries and discards_left > 0 and picked_batteries[-1] < battery:
            picked_batteries.pop()
            discards_left -= 1
        picked_batteries.append(battery)

    if discards_left > 0:
        picked_batteries = picked_batteries[:-discards_left]

    total += int(''.join(str(battery) for battery in picked_batteries))
    
print(total)

