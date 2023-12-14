
def toTranspose(grid):
    R, C = len(grid), len(grid[0])
    return ["".join(grid[r][c] for r in range(R)) for c in range(C)]

def read():
    problem = []
    with open("problem.txt") as problemFile:
        problem = [grid.split("\n") for grid in problemFile.read().split("\n\n")]

    return problem, [toTranspose(grid) for grid in problem]

def findFirstReflection(grid, forbidMultiple=False):
    for i in range(1, len(grid)):
        r = min(i, len(grid) - i)
        if grid[i-r:i] == grid[i+r-1:i-1:-1]:
            return i

    return 0

def partOne(problem):

    total = 0
    for grid, gridT in zip(*problem):
        total += 100 * findFirstReflection(grid) or findFirstReflection(gridT)

    print("Part 1: {:d}".format(total))

def findSmudgeReflection(grid):

    for i in range(1, len(grid)):
        r = min(i, len(grid) - i)

        differenceFound = False
        valid = True
        for drT, drB in zip(range(i-r, i), range(i+r-1, i-1, -1)):
            for c in range(len(grid[0])):
                if grid[drT][c] != grid[drB][c]:
                    if differenceFound:
                        valid = False
                        break
                    else:
                        differenceFound = True
            if not valid:
                break
        if valid and differenceFound:
            return i

    return 0

def partTwo(problem):

    total = 0
    for grid, gridT in zip(*problem):
        total += 100 * findSmudgeReflection(grid) or findSmudgeReflection(gridT)

    print("Part 2: {:d}".format(total))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 13, AoC 2023")

    problem = read();

    partOne(problem);
    partTwo(problem);

# 30890 too low