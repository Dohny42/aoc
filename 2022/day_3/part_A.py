from aocd import get_data
from string import ascii_letters

data = get_data(day=3, year=2022)

rucks = data.splitlines()


total_prio = 0

for ruck in rucks:
    first_half = set(ruck[:len(ruck)//2])
    second_half = set(ruck[len(ruck)//2:])

    duplicate = first_half.intersection(second_half).pop()

    total_prio += (ascii_letters.index(duplicate) + 1)

print(total_prio)
