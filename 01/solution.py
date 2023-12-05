import re

def read():
    with open("problem.txt") as problemFile:
        return [line.strip() for line in problemFile.readlines()]

def partOne(problem):

    digits = [re.findall("\d", line) for line in problem];
    total = sum(int(line[0] + line[-1]) for line in digits);

    print("Part 1: {:d}".format(total))

def partTwo(problem):

    digitNames = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    basePattern = "|".join(digitNames)
    reversePattern = "|".join(digitNames)[::-1]

    digitLookup = dict((k, str(n + 1)) for n, k in enumerate(digitNames))

    digitsForward = [re.findall("\d|" + basePattern, line) for line in problem];
    digitsReverse = [re.findall("\d|" + reversePattern, line[::-1]) for line in problem];

    getDigit = lambda d : digitLookup[d] if d in digitLookup else d

    total = sum(int(getDigit(f[0]) + getDigit(l[0][::-1])) for f, l in zip(digitsForward, digitsReverse));

    print("Part 2: {:d}".format(total))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 1, AoC 2023")

    problem = read();

    partOne(problem);
    partTwo(problem);
