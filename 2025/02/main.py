
with open("input.txt", "r") as file:
    ids = file.read().strip().split(",")

total = 0

for id_range in ids:
    first_id, last_id = id_range.split("-")
    first_id, last_id = int(first_id), int(last_id)
    
    for id in range(first_id, last_id + 1):
        s = str(id)
        half = len(s) // 2
        if s[half:] == s[:half]:
            total += id

print(total)


total = 0

for id_range in ids:
    first_id, last_id = id_range.split("-")
    first_id, last_id = int(first_id), int(last_id)
    
    for id in range(first_id, last_id + 1):
        s = str(id)
        is_valid = True
        for i in range(1, len(s)//2 + 1):
            if len(s) % i == 0 and s[:i] * (len(s)//i) == s:
                is_valid = False
        if not is_valid:
            total += id
            is_valid = True

print(total)
