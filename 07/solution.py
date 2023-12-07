
def read():
    problem = []
    cardMap = { "A": 14, "K": 13, "Q": 12, "J": 11, "T": 10 }
    with open("problem.txt") as problemFile:
        for line in problemFile.readlines():
            left, right = line.split(" ")
            hand = [cardMap[c] if c in cardMap else int(c) for c in left]
            bid = int(right.strip())
            problem.append((tuple(hand), bid))
    return problem

standardCache = {}
def standardEvaluator(hand):
    if hand not in standardCache:
        freq = [hand.count(c) for c in set(hand)]
        if (5 in freq):
            standardCache[hand] = (7, hand)
        elif (4 in freq):
            standardCache[hand] = (6, hand)
        elif (3 in freq and 2 in freq):
            standardCache[hand] = (5, hand)
        elif (3 in freq):
            standardCache[hand] = (4, hand)
        elif (freq.count(2) == 2):
            standardCache[hand] = (3, hand)
        elif (2 in freq):
            standardCache[hand] = (2, hand)
        else:
            standardCache[hand] = (1, hand)

    return standardCache[hand]

def partOne(problem):

    problem.sort(key=lambda x: standardEvaluator(x[0]))

    total = sum((n + 1) * bid for n, (_, bid) in enumerate(problem))

    print("Part 1: {:d}".format(total))

def partTwo(problem):

    problem = [(tuple(1 if c == 11 else c for c in hand), bid) for hand, bid in problem]

    cache = {}
    def optimalEvaluator(hand):
        if hand not in cache:
            newHand = optimizer(hand)
            freq = [newHand.count(c) for c in set(newHand)]

            if (5 in freq):
                cache[hand] = (7, hand)
            elif (4 in freq):
                cache[hand] = (6, hand)
            elif (3 in freq and 2 in freq):
                cache[hand] = (5, hand)
            elif (3 in freq):
                cache[hand] = (4, hand)
            elif (freq.count(2) == 2):
                cache[hand] = (3, hand)
            elif (2 in freq):
                cache[hand] = (2, hand)
            else:
                cache[hand] = (1, hand)

        return cache[hand]

    def optimizerHelper(hand, i):
        if i == 5:
            return (standardEvaluator(hand), hand)
        if hand[i] != 1:
            return optimizerHelper(hand, i+1)

        options = []
        for c in range(1, 15):
            if c == 11:
                continue
            newHand = (*hand[:i], c, *hand[i+1:])
            options.append(optimizerHelper(newHand, i+1))
        return max(options)

    def optimizer(hand):
        if 1 not in hand:
            return hand
        return optimizerHelper(hand, 0)[1]

    problem.sort(key=lambda x: optimalEvaluator(x[0]))

    total = sum((n + 1) * bid for n, (_, bid) in enumerate(problem))

    print("Part 2: {:d}".format(total))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 7, AoC 2023")

    problem = read();

    partOne(problem);
    partTwo(problem);
