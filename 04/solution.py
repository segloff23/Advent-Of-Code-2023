import re

def read():
    problem = []
    with open("problem.txt") as problemFile:
        for line in problemFile.readlines():
            match = re.match("Card *\d+:([^|]*)\|([^|]*)", line)
            winning, yours = match.group(1), match.group(2)
            problem.append((
                set(int(x.group()) for x in re.finditer("\d+", winning)),
                set(int(x.group()) for x in re.finditer("\d+", yours))
            ))
    return problem

def partOne(problem):
    
    total = 0
    for winning, yours in problem:
        wins = sum(1 if n in winning else 0 for n in yours)
        if (wins > 0):
            total += 2 ** (wins - 1)

    print("Part 1: {:d}".format(total))

def partTwo(problem):

    cache = {}
    def score(card):
        if card >= len(problem):
            return 0
        if card not in cache:
            winning, yours = problem[card]
            wins = sum(1 if n in winning else 0 for n in yours)
            if (wins > 0):
                cache[card] = 1 + sum(score(card + n + 1) for n in range(wins))
            else:
                cache[card] = 1
        return cache[card]

    total = sum(score(c) for c in range(len(problem)))

    print("Part 2: {:d}".format(total))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 4, AoC 2023")

    problem = read();

    partOne(problem);
    partTwo(problem);
