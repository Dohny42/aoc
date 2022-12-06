from aocd import get_data

data = get_data(day=5, year=2022)

init_stacks, procedure = data.split("\n\n")

init_stacks_rows = init_stacks.splitlines()

num_of_stacks = len(init_stacks_rows[-1].split())

stacks = []

# parsing stacks
for j in range(1, num_of_stacks * 4, 4):
    stack = []
    for row in init_stacks_rows[:-1]:
        c = row[j]
        if c != " ":
            stack.append(c)
    stacks.append(stack[::-1])

# procedure
for instruction in procedure.splitlines():
    splitted = instruction.split()
    count = int(splitted[1])
    stack_from_idx = int(splitted[3]) - 1
    stack_to_idx = int(splitted[5]) - 1

    stack_to_append = stacks[stack_from_idx][-count:]

    stacks[stack_to_idx].extend(stack_to_append)
    del stacks[stack_from_idx][-count:]

# getting the message
msg = ""
for stack in stacks:
    msg += stack[-1]

print(msg)
