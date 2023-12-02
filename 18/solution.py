
def read():
    problem = []
    with open("problem.txt") as problemFile:
        problem = list(map(int, problemFile.readlines()))

    return problem

def partOne(problem):

    print("Part 1: {:d}".format(0))

def partTwo(problem):

    print("Part 2: {:d}".format(0))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 18, AoC 2022")

    problem = read();

    partOne(problem);
    partTwo(problem);
