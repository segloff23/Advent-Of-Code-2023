
def read():
    with open("problem.txt") as problemFile:
        return [list(map(int, line.split(" "))) for line in problemFile.readlines()]

def partOneTwo(problem):

    total, total2 = 0, 0
    for row in problem:
        N = len(row)
        i = 1
        total += row[-1]
        total2 += i * row[0]
        while not all(x == 0 for x in row):
            row = [row[i] - row[i-1] for i in range(1, N)]
            N -= 1
            i *= -1
            total += row[-1]
            total2 += i * row[0]

    print("Part 1: {:d}".format(total))

    print("Part 2: {:d}".format(total2))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 9, AoC 2023")

    problem = read();

    partOneTwo(problem);
