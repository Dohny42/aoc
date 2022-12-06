from aocd import get_data

data = get_data(day=6, year=2022)

dummy_data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

total = 14
for i in range(len(data) - 13):
    buffer_set = set(data[i:i+14])
    if len(buffer_set) != 14:
        total += 1
        continue
    else:
        break

print(total)
