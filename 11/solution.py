
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

    distances = []
    for n1 in range(L-1):
        r1, c1 = nodes[n1]
        for n2 in range(n1+1, L):
            r2, c2 = nodes[n2]
            d = abs(r2 - r1) + abs(c2 - c1)
            rowGaps = sum(1 for b in blankRows if (b > r1 and b < r2) or (b > r2 and b < r1))
            colGaps = sum(1 for b in blankCols if (b > c1 and b < c2) or (b > c2 and b < c1))
            distances.append((d, rowGaps, colGaps))

    weight = lambda d, N: d[0] + (N - 1) * (d[1] + d[2])

    total = sum(weight(d, 2) for d in distances)
    total2 = sum(weight(d, 1000000) for d in distances)

    print("Part 1: {:d}".format(total))
    print("Part 2: {:d}".format(total2))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 11, AoC 2023")

    problem = read();

    partOneTwo(problem);
