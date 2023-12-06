import re
import math

def read():
    with open("problem.txt") as problemFile:
        timeRaw, distanceRaw = problemFile.readlines()
        time = [int(x) for x in re.split(" +", timeRaw.split(":")[1].strip())]
        distance = [int(x) for x in re.split(" +", distanceRaw.split(":")[1].strip())]
        problem = list(zip(time, distance))
    return problem

def calculateRaceMargin(T, D):

    if not (T**2 > 4*D):
        return 0

    low = math.ceil((1 / 2) * (T - (T**2 - 4*D)**0.5))
    high = math.floor((1 / 2) * (T + (T**2 - 4*D)**0.5))

    if not (low * (T - low) > D):
        low += 1
    if not (high * (T - high) > D):
        high -= 1

    return high - low + 1

def partOne(problem):

    product = 1
    for T, D in problem:
        product *= calculateRaceMargin(T, D)

    print("Part 1: {:d}".format(product))

def partTwo(problem):

    T = int("".join(str(t[0]) for t in problem))
    D = int("".join(str(d[1]) for d in problem))

    total = calculateRaceMargin(int(T), int(D))

    print("Part 2: {:d}".format(total))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 6, AoC 2023")

    problem = read();

    partOne(problem);
    partTwo(problem);
