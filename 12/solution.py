
def read():
    problem = []
    with open("problem.txt") as problemFile:
        problem = []
        for line in problemFile.readlines():
            text, rawPattern = line.split(" ")
            pattern = tuple(map(int, rawPattern.split(",")))
            problem.append((text, pattern))
    return problem

def truncateText(text):
    i = 0
    while i < len(text) and text[i] == ".":
        i += 1
    return text[i:]

cache = {}
def DP(text, pattern):
    def DPHelper(subproblem):
        if subproblem not in cache:
            patternRemaining, textRemaining = subproblem
            if len(patternRemaining) == 0:
                cache[subproblem] = int(textRemaining.count("#") == 0)
            elif len(textRemaining) == 0:
                cache[subproblem] = 0
            else:
                G = patternRemaining[0]
                T = len(textRemaining)
                if G > T:
                    cache[subproblem] = 0
                else:
                    total = 0
                    for i in range(0, T - G + 1):
                        if textRemaining[0:i].count("#") != 0:
                            break
                        if textRemaining[i:i+G].count(".") == 0:
                            if i+G == T or textRemaining[i+G] != "#":
                                total += DPHelper((tuple(patternRemaining[1:]), truncateText(textRemaining[i+G+1:])))
                    cache[subproblem] = total
        return cache[subproblem]

    return DPHelper((pattern, truncateText(text)))

def partOne(problem):

    total = 0
    for text, pattern in problem:
        total += DP(text, pattern)

    print("Part 1: {:d}".format(total))

def partTwo(problem):

    total = 0
    for text, pattern in problem:
        total += DP("?".join(text for i in range(5)), pattern*5)

    print("Part 2: {:d}".format(total))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 12, AoC 2022")

    problem = read();

    partOne(problem);
    partTwo(problem);
