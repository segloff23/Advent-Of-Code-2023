
def read():
    with open("problem.txt") as problemFile:
        data = [line.strip() for line in problemFile.readlines()]
        blankRows = set(r for r, row in enumerate(data) if row.count("#") == 0)
        blankCols = set(c for c in range(len(data[0])) if sum(1 for row in data if row[c] == "#") == 0)
        nodes = [(r, c) for r, row in enumerate(data) for c, col in enumerate(row) if col == "#"]
    return (nodes, blankRows, blankCols)

def partOneTwo(problem):

    nodes, blankRows, blankCols = problem
    L = len(nodes)

    total = 0
    total2 = 0
    for n1 in range(L-1):
        r1, c1 = nodes[n1]
        for n2 in range(n1+1, L):
            r2, c2 = nodes[n2]
            d = abs(r2 - r1) + abs(c2 - c1)
            rowGaps = sum(1 for b in blankRows if (b > r1 and b < r2) or (b > r2 and b < r1))
            colGaps = sum(1 for b in blankCols if (b > c1 and b < c2) or (b > c2 and b < c1))
            total += d + (rowGaps + colGaps)
            total2 += d + (1000000 - 1) * (rowGaps + colGaps)

    print("Part 1: {:d}".format(total))
    print("Part 2: {:d}".format(total2))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 11, AoC 2023")

    problem = read();

    partOneTwo(problem);
