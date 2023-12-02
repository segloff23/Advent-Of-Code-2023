
contents = """
def read():
    problem = []
    with open("problem.txt") as problemFile:
        problem = list(map(int, problemFile.readlines()))

    return problem

def partOne(problem):

    print("Part 1: {{:d}}".format(0))

def partTwo(problem):

    print("Part 2: {{:d}}".format(0))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day {:s}, AoC 2023")

    problem = read();

    partOne(problem);
    partTwo(problem);
"""

import os
import sys

if __name__ == "__main__":

    day = sys.argv[1]

    try:
        os.mkdir("./{}".format(day))
    except FileExistsError:
        print("Day {} has already been created".format(day))
        sys.exit(0)

    with open("{}/solution.py".format(day), "w") as f:
        f.write(contents.format(day))
    with open("{}/problem.txt".format(day), "w") as f:
        f.write("")

