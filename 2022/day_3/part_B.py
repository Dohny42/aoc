from aocd import get_data
from string import ascii_letters

data = get_data(day=3, year=2022)

rucks = data.splitlines()

total_prio = 0

for i in range(0, len(rucks) - 2, 3):
    group = rucks[i:i+3]
    group_rucks_sets = []

    for ruck in group:
        ruck_set = set(ruck)
        group_rucks_sets.append(ruck_set)

    duplicate = group_rucks_sets[0].intersection(group_rucks_sets[1])
    duplicate.intersection_update(group_rucks_sets[2])

    total_prio += (ascii_letters.index(duplicate.pop()) + 1)

print(total_prio)
