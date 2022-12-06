from aocd import get_data

data = get_data(day=2, year=2022)


rounds = data.splitlines()


shapes_map = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

shapes_score_map = {
    "X": 1,
    "Y": 2,
    "Z": 3
}


total_score = 0

for round in rounds:
    opp_shape, my_shape = round.split(" ")
    opp_shape_mapped = shapes_map[opp_shape]

    my_score = shapes_score_map[my_shape]

    total_score += my_score

    # draw
    if opp_shape_mapped == my_shape:
        total_score += 3
        continue

    # loss
    if opp_shape == "A" and my_shape == "Z":
        continue
    if opp_shape == "B" and my_shape == "X":
        continue
    if opp_shape == "C" and my_shape == "Y":
        continue

    # win
    if my_shape == "X" and opp_shape == "C":
        total_score += 6
        continue
    if my_shape == "Y" and opp_shape == "A":
        total_score += 6
        continue
    if my_shape == "Z" and opp_shape == "B":
        total_score += 6
        continue


print(total_score)
