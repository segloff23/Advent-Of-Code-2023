import re

def read():
    problem = []
    with open("problem.txt") as problemFile:
        problem = problemFile.read().split("\n\n")
        seeds = [int(x) for x in problem[0].split(" ")[1:]]

        relationships = {}
        data = {}
        for mapping in problem[1:]:
            lines = mapping.split("\n")
            mapNamesMatcher = re.match(r"([^-]+)\-to\-([^-]+) map:", lines[0])
            mapNames = mapNamesMatcher.groups()
            relationships[mapNames[0]] = mapNames[1]
            data[mapNames[0]] = [tuple(map(int, row.split(" "))) for row in lines[1:]]

    return (seeds, relationships, data)

def processInterval(inputIntervals, intervalMaps):
    outputIntervals = []
    while inputIntervals:
        start, end = inputIntervals.pop()
        found = False
        for dest, src, rng in intervalMaps:
            low = src
            high = src + rng - 1
            offset = dest - src
            # (low [start high) end]
            if (low <= start and start <= high and high <= end):
                if high != end:
                    inputIntervals = [(high + 1, end)] + inputIntervals
                outputIntervals.append((start+offset, high+offset))
                found = True
                break
            # (start [low end] high)
            elif (start <= low and low <= end and end <= high):
                if start != low:
                    inputIntervals = [(start, low - 1)] + inputIntervals
                outputIntervals.append((low+offset, end+offset))
                found = True
                break
            # (start [low high] end)
            elif (start <= low and high <= end):
                if start != low:
                    inputIntervals = [(start, low - 1)] + inputIntervals
                if high != end:
                    inputIntervals = [(high + 1, end)] + inputIntervals
                outputIntervals.append((low+offset, high+offset))
                found = True
                break
            # (low [start end] high)
            elif (low <= start and end <= high):
                outputIntervals.append((start+offset, end+offset))
                found = True
                break
        if (not found):
            outputIntervals.append((start, end))
    return outputIntervals

def partOne(problem):

    seeds, relationships, data = problem

    currentMap = "seed"
    currentIntervals = [(s, s) for s in seeds]
    while currentMap != "location":
        currentIntervals = processInterval(currentIntervals, data[currentMap])
        currentMap = relationships[currentMap]

    best = min(x[0] for x in currentIntervals)

    print("Part 1: {:d}".format(best))

def partTwo(problem):
    
    seeds, relationships, data = problem

    currentMap = "seed"
    currentIntervals = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]
    while currentMap != "location":
        currentIntervals = processInterval(currentIntervals, data[currentMap])
        currentMap = relationships[currentMap]

    best = min(x[0] for x in currentIntervals)

    print("Part 2: {:d}".format(best))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 5, AoC 2023")

    problem = read();

    partOne(problem);
    partTwo(problem);
