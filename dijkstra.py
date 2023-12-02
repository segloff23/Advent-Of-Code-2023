import heapq;

class Graph:

    def __init__(self):
        pass;

    def getNeighbors(self, node):
        return [];

    def getDistance(self, current, new):
        return 0;

class DijkstraStepper:

    def __init__(self, graph, source, dest):

        self.graph = graph;
        self.source = source;
        self.dest = dest;

        self.reset();

    def reset(self):

        self.finalized = set();
        self.pi = {self.source: (None, 0)};

        self.heap = [];
        heapq.heappush(self.heap, (0, self.source));

        self.last = None;
        self.current = self.source;
        self.isDone = False;

    def updatePi(self, node, value):
        self.pi[node] = value;

    def step(self):

        baseDist = self.pi[self.current][1];
        for neighbor in self.graph.getNeighbors(self.current):
            if neighbor not in self.finalized:
                dist = self.graph.getDistance(self.current, neighbor);
                if (dist != None):
                    if (neighbor not in self.pi):
                        self.pi[neighbor] = (self.current, dist + baseDist);
                        heapq.heappush(self.heap, (dist+baseDist, neighbor))

                    elif (dist + baseDist < self.pi[neighbor][1]):
                        self.pi[neighbor] = (self.current, dist + baseDist);
                        heapq.heappush(self.heap, (dist+baseDist, neighbor))

        if (self.current == self.dest):
            self.last = self.current;
            self.isDone = True;
        else:
            self.finalized.add(self.current);
            self.last = self.current;
            self.current = None;
            if (len(self.heap) != 0):
                _, smallest = heapq.heappop(self.heap);
                if (self.pi[smallest][1] != None):
                    self.current = smallest;
            self.isDone = (self.current == None);

    def constructPath(self, end):

        path = [];
        current = end;
        while (self.pi[current][0] != None):
            path.append(current);
            current = self.pi[current][0];
        path.append(current);

        return list(reversed(path));

class Dijkstra:

    def solve(graph, source, dest):

        forward = DijkstraStepper(graph, source, dest);
        backward = DijkstraStepper(graph, dest, source);

        while (not (forward.isDone or backward.isDone)):

            forward.step();
            backward.step();

            if (forward.last == dest):

                dist = forward.pi[forward.last][1];
                route = forward.constructPath(dest)

                return (route, dist);

            elif (backward.last == source):

                dist = forward.pi[backward.last][1];
                route = list(reversed(backward.constructPath(source)));

                return (route, dist);

            elif (forward.last in backward.pi) or (backward.last in forward.pi):

                w = forward.last if (forward.last in backward.pi) else backward.last;
                dist = forward.pi[w][1] + backward.pi[w][1];

                for x in forward.pi:
                    if (x in backward.pi):
                        newDist = forward.pi[x][1] + backward.pi[x][1];
                        if (newDist < dist):
                            w = x;
                            dist = newDist;

                routeF = forward.constructPath(w);
                routeB = backward.constructPath(w);
                route = routeF[:-1] + list(reversed(routeB));

                return (route, dist);

        return ([], None);

    def oneWaySolve(graph, source, dest):

        forward = DijkstraStepper(graph, source, dest);

        while (not forward.isDone):

            forward.step();

            if (forward.last == dest):

                dist = forward.pi[forward.last][1];
                route = forward.constructPath(dest)

                return (route, dist);

        return ([], None);