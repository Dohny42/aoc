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

    # need to loose
    if my_shape == "X":
        if opp_shape == "A":
            total_score += shapes_score_map["Z"]
            continue
        elif opp_shape == "B":
            total_score += shapes_score_map["X"]
            continue
        elif opp_shape == "C":
            total_score += shapes_score_map["Y"]
            continue

    # need to draw
    if my_shape == "Y":
        total_score += (3 + shapes_score_map[opp_shape_mapped])
        continue

    # need to win
    if my_shape == "Z":
        total_score += 6
        if opp_shape == "A":
            total_score += shapes_score_map["Y"]
            continue
        elif opp_shape == "B":
            total_score += shapes_score_map["Z"]
            continue
        elif opp_shape == "C":
            total_score += shapes_score_map["X"]
            continue

print(total_score)
