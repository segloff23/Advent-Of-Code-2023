
def read():
    problem = []
    cardMap = { "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10 }
    with open("problem.txt") as problemFile:
        for line in problemFile.readlines():
            left, right = line.split(" ")
            hand = tuple(cardMap[c] if c in cardMap else int(c) for c in left)
            bid = int(right.strip())
            problem.append((hand, bid))
    return problem

def evaluateType(hand):
    freq = [hand.count(c) for c in set(hand)]
    if (5 in freq):
        return 7
    elif (4 in freq):
        return 6
    elif (3 in freq and 2 in freq):
        return 5
    elif (3 in freq):
        return 4
    elif (freq.count(2) == 2):
        return 3
    elif (2 in freq):
        return 2
    else:
        return 1

typeCache = {}
def evaluateCachedType(hand):
    if hand not in typeCache:
        typeCache[hand] = evaluateType(hand)

    return typeCache[hand]

def partOne(problem):
    problem.sort(key=lambda x: (evaluateType(x[0]), x[0]))
    total = sum((n + 1) * bid for n, (_, bid) in enumerate(problem))

    print("Part 1: {:d}".format(total))

def partTwo(problem):
    problem = [(tuple(1 if c == 11 else c for c in hand), bid) for hand, bid in problem]

    optimalCache = {}
    def optimalEvaluator(hand):
        if hand not in optimalCache:
            newHand = optimizer(hand)
            optimalCache[hand] = (evaluateType(newHand), hand)

        return optimalCache[hand]

    def optimizer(hand):
        jokers = hand.count(1)
        if jokers == 0:
            return hand
        if jokers == 5:
            return (14, 14, 14, 14, 14)

        maxFreq = max(hand.count(c) for c in hand)
        options = [c for c in hand if hand.count(c) == maxFreq if c != 1]
        replacement = max(options, default = max(hand))

        return tuple(replacement if c == 1 else c for c in hand)

    problem.sort(key=lambda x: optimalEvaluator(x[0]))

    total = sum((n + 1) * bid for n, (_, bid) in enumerate(problem))

    print("Part 2: {:d}".format(total))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 7, AoC 2023")

    problem = read();

    partOne(problem);
    partTwo(problem);
