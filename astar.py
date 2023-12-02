
import heapq

class Graph:

    def __init__(self):
        pass

    def getNeighbors(self, node):
        return []

    def getDistance(self, current, target):
        return 0

    def getHeuristic(self, node):
        return 0

    def isGoal(self, node):
        return 0

class DijkstraStepper:

    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.reset()

    def reset(self):

        self.finalized = set()
        self.pi = {self.source: (None, 0)}

        self.heap = []
        heapq.heappush(self.heap, (0, self.source))

        self.last = None
        self.current = self.source
        self.isDone = False

    def updatePi(self, node, value):
        self.pi[node] = value

    def step(self):

        baseDist = self.pi[self.current][1]
        for neighbor in self.graph.getNeighbors(self.current):
            if neighbor not in self.finalized:
                dist = self.graph.getDistance(self.current, neighbor)
                if (dist != None):
                    if (neighbor not in self.pi):
                        self.pi[neighbor] = (self.current, dist + baseDist)
                        heapq.heappush(self.heap, (dist+baseDist, neighbor))

                    elif (dist + baseDist < self.pi[neighbor][1]):
                        self.pi[neighbor] = (self.current, dist + baseDist)
                        heapq.heappush(self.heap, (dist+baseDist, neighbor))

        if (self.graph.isGoal(self.current)):
            self.last = self.current
            self.isDone = True
        else:
            self.finalized.add(self.current)
            self.last = self.current
            self.current = None
            if (len(self.heap) != 0):
                _, smallest = heapq.heappop(self.heap)
                if (self.pi[smallest][1] != None):
                    self.current = smallest
            self.isDone = (self.current == None)

    def constructPath(self, end):

        path = []
        current = end
        while (self.pi[current][0] != None):
            path.append(current)
            current = self.pi[current][0]
        path.append(current)

        return list(reversed(path))

class AstarStepper:

    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.reset()

    def reset(self):

        self.finalized = set()
        self.gScore = {self.source: 0}

        self.fScore = {self.source: self.graph.getHeuristic(self.source)}

        self.openSet = []
        self.cameFrom = {}

        self.last = None
        self.current = self.source
        self.isDone = False

    def step(self):

        for neighbor in self.graph.getNeighbors(self.current):
            gScoreTent = self.gScore[self.current] + self.graph.getDistance(self.current, neighbor)
            if neighbor not in self.gScore or gScoreTent < self.gScore[neighbor]:
                self.cameFrom[neighbor] = self.current
                self.gScore[neighbor] = gScoreTent
                self.fScore[neighbor] = gScoreTent + self.graph.getHeuristic(neighbor)
                heapq.heappush(self.openSet, (self.fScore[neighbor], neighbor))

        if (self.graph.isGoal(self.current)):
            self.last = self.current
            self.isDone = True
        else:
            self.finalized.add(self.current)
            self.last = self.current
            self.current = None
            if (len(self.openSet) != 0):
                _, self.current = heapq.heappop(self.openSet)
            self.isDone = (self.current == None)

    def reconstructPath(self, current):

        path = [current]
        while (current in self.cameFrom):
            current = self.cameFrom[current]
            path.append(current)

        return path[-1::-1]

class Astar:

    def solve(graph, source):

        forward = AstarStepper(graph, source)
        backward = AstarStepper(graph, source)
        while (not (forward.isDone or backward.isDone)):

            forward.step()
            backward.step()

            if (graph.isGoal(forward.current)):
                return forward.reconstructPath(forward.current)
            elif (backward.current == source):
                return backward.reconstructPath(goal)[-1::-1]
            elif (forward.current in backward.gScore) or (backward.current in forward.gScore):

                w = forward.current if (forward.current in backward.gScore) else backward.current
                dist = forward.gScore[w] + backward.gScore[w]

                for x in forward.gScore:
                    if (x in backward.gScore):
                        newDist = forward.gScore[x] + backward.gScore[x]
                        if (newDist < dist):
                            w = x
                            dist = newDist

                routeF = forward.reconstructPath(w)
                routeB = backward.reconstructPath(w)

                return routeF[:-1] + routeB[-1::-1]

        return None

    def oneWaySolve(graph, source, goal):

        forward = AstarStepper(graph, source, goal)
        while (not forward.isDone):

            forward.step()

            if (forward.last == goal):
                return forward.reconstructPath(goal)

        return None

