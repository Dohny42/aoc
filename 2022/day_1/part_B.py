from aocd import get_data

data = get_data(day=1, year=2022)

calories_lines = data.split("\n\n")

calories_sums = [sum(map(int, calories.split("\n")))
                 for calories in calories_lines]

calories_sums_sorted = sorted(calories_sums, reverse=True)
top_three_sums = sum(calories_sums_sorted[:3])

print(top_three_sums)
