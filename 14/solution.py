import re

def read():
    problem = []
    with open("problem.txt") as problemFile:
        problem = [line for line in problemFile.read().split("\n")]

    return problem

def partOne(problem):

    R, C = len(problem), len(problem[0])
    total = 0
    for c in range(C):
        col = "".join(problem[r][c] for r in range(R))
        for m in re.finditer(r"(\.|O)+", col):
            H = R - m.span()[0]
            L = H - m.group().count("O") + 1
            total += (H + 1 - L) * (H + L) // 2

    print("Part 1: {:d}".format(total))

def partTwo(problem):

    def replacer(m):
        text = m.group()
        L = len(text)
        N = text.count("O")
        return "O" * N + (L - N) * "."

    R, C = len(problem), len(problem[0])

    grid = tuple(problem)
    seen = {}
    loop = []
    ctr = 0
    while grid not in seen:
        seen[grid] = ctr
        loop.append(sum(row.count("O") * (R - r) for r, row in enumerate(grid)))
        for d in range(4):
            newGrid = []
            for c in range(C):
                col = "".join(grid[r][c] for r in range(R))
                col = re.sub(r"(\.|O)+", replacer, col)
                newGrid.append(col)
            R, C = C, R
            grid = tuple(row[::-1] for row in newGrid)
        ctr += 1

    L = ctr - seen[grid]
    i = ((1000000000 - seen[grid]) % L) - L

    total = loop[i]

    print("Part 2: {:d}".format(total))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 14, AoC 2023")

    problem = read();

    partOne(problem);
    partTwo(problem);
