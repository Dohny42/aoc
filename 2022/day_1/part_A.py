from aocd import get_data

data = get_data(day=1, year=2022)

calories_lines = data.split("\n\n")

calories_sums = [sum(map(int, calories.split("\n")))
                 for calories in calories_lines]

max = max(calories_sums)

print(max)
