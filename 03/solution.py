import re

def read():
    problem = []
    with open("problem.txt") as problemFile:
        problem = [line.strip() for line in problemFile.readlines()]

    C = len(problem[0])
    problem = ["." * (C+2)] + ["." + line + "." for line in problem] + ["." * (C+2)]

    return problem

def partOne(problem):

    total = 0
    for r in range(1, len(problem)-1):
        line = problem[r]
        for match in re.finditer("([0-9]+)", line):
            span = match.span()
            value = int(match.group())
            searches = [
                (r-1, span[0]-1, span[1]+1), # above
                (r+1, span[0]-1, span[1]+1), # below
                (r, span[0]-1, span[0]), # left
                (r, span[1], span[1]+1) # right
            ]
            for rs, cs0, cs1 in searches:
                if re.search("[^0-9.]", problem[rs][cs0:cs1]):
                    total += value

    print("Part 1: {:d}".format(total))

def partTwo(problem):

    gears = {}
    for r in range(1, len(problem)-1):
        line = problem[r]
        for match in re.finditer("([0-9]+)", line):
            span = match.span()
            value = int(match.group())
            searches = [
                (r-1, span[0]-1, span[1]+1), # above
                (r+1, span[0]-1, span[1]+1), # below
                (r, span[0]-1, span[0]), # left
                (r, span[1], span[1]+1) # right
            ]
            for rs, cs0, cs1 in searches:
                for gearMatch in re.finditer("\*", problem[rs][cs0:cs1]):
                    c = cs0 + gearMatch.span()[0]
                    gears.setdefault((rs, c), [])
                    gears[(rs, c)].append(value)

    total = 0
    for gear, values in gears.items():
        if len(values) == 2:
            total += values[0] * values[1]

    print("Part 2: {:d}".format(total))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 3, AoC 2023")

    problem = read();

    partOne(problem);
    partTwo(problem);
