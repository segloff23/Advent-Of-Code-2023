
def read():
    problem = []
    with open("problem.txt") as problemFile:
        problem = ["." + line.strip() + "." for line in problemFile.readlines()]
        problem = ["."*len(problem[0])] + problem + ["."*len(problem[0])]
    return problem


faces = {
    "|": [ 1, -1 ],
    "-": [ 1j, -1j ],
    "L": [ -1,  1j ],
    "J": [ -1, -1j ],
    "7": [  1, -1j ],
    "F": [  1,  1j ],
    ".": [],
}

def partOne(problem):

    R, C = len(problem), len(problem[0])

    source = None
    for r in range(R):
        for c in range(C):
            if problem[r][c] == "S":
                source = r + 1j*c
        if source:
            break

    sourceFaces = []
    for drc in [1, -1, 1j, -1j]:
        node = source + drc
        r, c = int(node.real), int(node.imag)
        if -1*drc in faces[problem[r][c]]:
            sourceFaces.append(drc)
    faces["S"] = sourceFaces


    loop = {}

    dist = 0
    cameFrom = sourceFaces[0]
    node = source
    while node not in loop:
        loop[node] = dist
        dist += 1
        r, c = int(node.real), int(node.imag)
        A, B = faces[problem[r][c]]
        if A != -1*cameFrom:
            node += A
            cameFrom = A
        else:
            node += B
            cameFrom = B

    maxDist = (len(loop) // 2) + (len(loop) % 2)

    print("Part 1: {:d}".format(maxDist))

    return source, loop

def partTwo(problem, source, loop):

    R, C = len(problem), len(problem[0])

    shrinkLoop = set()
    for node in loop:
        r, c = int(node.real), int(node.imag)
        directions = faces[problem[r][c]]
        for d in directions:
            shrinkLoop.add(node + 0.5*d)
        shrinkLoop.add(node)

    outside = set()
    queue = [0]

    while queue:
        node = queue.pop()
        outside.add(node)
        for d in [0.5, -0.5, 0.5j, -0.5j]:
            neighbor = node + d
            r, c = int(neighbor.real), int(neighbor.imag)
            if (r < 0 or r >= R or c < 0 or c >= C):
                continue
            if (neighbor in outside):
                continue
            if (neighbor in shrinkLoop):
                continue
            queue.append(neighbor)

    outside = set(node for node in outside if int(node.real) == node.real and int(node.imag) == node.imag)
    area = (R * C) - len(outside) - len(loop)

    print("Part 2: {:d}".format(area))

# %% MAIN CALLS
if __name__ == "__main__":

    print("Solving Day 10, AoC 2023")

    problem = read();

    source, loop = partOne(problem);
    partTwo(problem, source, loop);
