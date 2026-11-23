import heapq
import math

def read_input(filename):
    with open(filename, 'r') as f:
        tokens = f.read().split('\n')
    tokens = [t.strip() for t in tokens if t.strip() != '']
    idx = 0

    coords = {}
    n_vertices = int(tokens[idx]); idx += 1
    for _ in range(n_vertices):
        parts = tokens[idx].split(); idx += 1
        node, x, y = parts[0], float(parts[1]), float(parts[2])
        coords[node] = (x, y)

    adjlist = {node: [] for node in coords}
    n_edges = int(tokens[idx]); idx += 1
    for _ in range(n_edges):
        parts = tokens[idx].split(); idx += 1
        n1, n2, cost = parts[0], parts[1], float(parts[2])
        adjlist[n1].append((n2, cost))   # directed — matches your spec, no reverse edge

    start = tokens[idx].strip(); idx += 1
    goal = tokens[idx].strip(); idx += 1

    return coords, adjlist, start, goal


def heuristic(node, goal, coords):
    x1, y1 = coords[node]
    x2, y2 = coords[goal]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


class NodeState:
    _counter = 0

    def __init__(self, node_id, g, f, parent=None):
        self.node_id = node_id
        self.g = g
        self.f = f
        self.parent = parent
        NodeState._counter += 1
        self.order = NodeState._counter

    def __lt__(self, other):
        if self.f != other.f:
            return self.f < other.f
        return self.order < other.order


def reconstruct_path(node_state):
    path = []
    while node_state is not None:
        path.append(node_state.node_id)
        node_state = node_state.parent
    return path[::-1]


def a_star(coords, adjlist, start, goal):
    minQ = []
    start_state = NodeState(start, g=0, f=heuristic(start, goal, coords))
    heapq.heappush(minQ, start_state)

    closed = set()  # lazy-deletion optimization; doesn't change the result

    while minQ:
        N = heapq.heappop(minQ)

        if N.node_id in closed:
            continue

        if N.node_id == goal:
            path = reconstruct_path(N)
            print("Solution path:", " – ".join(path))
            print("Solution cost:", N.g)
            return path, N.g

        closed.add(N.node_id)

        for M, edge_cost in adjlist.get(N.node_id, []):
            g = N.g + edge_cost
            h = heuristic(M, goal, coords)
            f = g + h
            N_prime = NodeState(M, g, f, parent=N)
            heapq.heappush(minQ, N_prime)

    print("No path found from", start, "to", goal)
    return None, math.inf


def run(filename="input.txt"):
    coords, adjlist, start, goal = read_input(filename)
    return a_star(coords, adjlist, start, goal)