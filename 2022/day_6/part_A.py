from aocd import get_data

data = get_data(day=6, year=2022)

dummy_data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

total = 4
for i in range(len(data) - 3):
    buffer_set = set(data[i:i+4])
    if len(buffer_set) != 4:
        total += 1
        continue
    else:
        break

print(total)
