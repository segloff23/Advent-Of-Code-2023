import re

def read():
    problem = {}
    
    pattern = "Game (?P<id>\d+):(?P<drawString>(;?(,? \d+ [a-z]+)*)*)"

    parseItem = lambda item: (item[1].strip(), int(item[0]))

    with open("problem.txt") as problemFile:
        for line in problemFile.readlines():
            matchResult = re.match(pattern, line).groupdict()
            gameId = int(matchResult["id"])
            drawSets = [
                dict(parseItem(item.strip().split(" ")) for item in val.split(","))
                for val in matchResult["drawString"].split(";")
            ]
            problem[int(gameId)] = drawSets

    return problem

def partOne(problem):

    hypothesis = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    total = 0
    for gameId, game in problem.items():
        invalid = False
        for draw in game:
            for color in hypothesis:
                if color in draw and hypothesis[color] < draw[color]:
                    invalid = True
                    break
            if invalid:
                break
        if not invalid:
            total += gameId

    print("Part 1: {:d}".format(total))

def partTwo(problem):
    
    colors = ["red", "blue", "green"]

    colorMax = lambda color: lambda draw: draw[color] if color in draw else 0

    total = 0
    for game in problem.values():
        power = 1
        for c in colors:
            power *= max(game, key=colorMax(c))[c]
        total += power

    print("Part 2: {:d}".format(total))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 2, AoC 2023")

    problem = read();

    partOne(problem);
    partTwo(problem);

