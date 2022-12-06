from aocd import get_data

data = get_data(day=4, year=2022)


pairs = [line.split(",") for line in data.splitlines()]

num_of_overlaps = 0
for first, second in pairs:
    first_section = tuple(map(int, first.split("-")))
    second_section = tuple(map(int, second.split("-")))

    # first in second check
    if (second_section[0] <= first_section[0] <= second_section[1] and
            second_section[0] <= first_section[1] <= second_section[1]):
        num_of_overlaps += 1
        continue
    # second in first check
    if (first_section[0] <= second_section[0] <= first_section[1] and
            first_section[0] <= second_section[1] <= first_section[1]):
        num_of_overlaps += 1
        continue

print(num_of_overlaps)
