import math
import re

def read():
    problem = []
    with open("problem.txt") as problemFile:
        LR = { "L": 0, "R": 1 }
        instructions, rest = problemFile.read().split("\n\n")
        instructions = [LR[i] for i in instructions]
        lookup = {}
        for line in rest.split("\n"):
            a, b, c = re.match(r"(\w+) = \((\w+), (\w+)\)", line).groups()
            lookup[a] = (b, c)
        problem = (instructions, lookup)

    return problem

def partOne(problem):
    instructions, lookup = problem
    N = len(instructions)

    current, goal = "AAA", "ZZZ"
    i, steps = 0, 0
    while current != goal:
        current = lookup[current][instructions[i]]
        i += 1
        i %= N
        steps += 1

    print("Part 1: {:d}".format(steps))

def partTwo(problem):
    instructions, lookup = problem
    N = len(instructions)

    starts = set(word for word in lookup if word[-1] == "A")
    goals = set(word for word in lookup if word[-1] == "Z")

    stepList = []
    for s in starts:
        goal = None
        current = s
        i, steps = 0, 0
        while not goal:
            current = lookup[current][instructions[i]]
            i += 1
            i %= N
            steps += 1
            if current in goals:
                goal = steps
        stepList.append(goal)
    
    minSteps = math.lcm(*stepList)

    print("Part 2: {:d}".format(minSteps))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 8, AoC 2023")

    problem = read();

    partOne(problem);
    partTwo(problem);
