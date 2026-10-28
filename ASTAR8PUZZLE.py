
import heapq

def heuristic(state, goal):
    return sum(1 for i in range(9)
               if state[i] != 0 and state[i] != goal[i])

def astar(start, goal):
    pq = [(heuristic(start, goal), 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, state = heapq.heappop(pq)

        if g != cost[state]:
            continue

        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            path.reverse()

            print("Solution found!")
            print("Moves:", len(path) - 1)
            for s in path:
                print(s[:3])
                print(s[3:6])
                print(s[6:])
                print()
            return

        zero = state.index(0)
        row, col = divmod(zero, 3)

        moves = []
        if row > 0:
            moves.append(zero - 3)
        if row < 2:
            moves.append(zero + 3)
        if col > 0:
            moves.append(zero - 1)
        if col < 2:
            moves.append(zero + 1)

        for pos in moves:
            new = list(state)
            new[zero], new[pos] = new[pos], new[zero]
            new = tuple(new)
            ng = g + 1

            if ng < cost.get(new, float('inf')):
                cost[new] = ng
                parent[new] = state
                heapq.heappush(
                    pq, (ng + heuristic(new, goal), ng, new)
                )

    print("No solution found")

def read_state(message):
    print(message)
    s = []
    for _ in range(3):
        s.extend(map(int, input().split()))
    if sorted(s) != list(range(9)):
        raise ValueError("Enter digits 0 to 8 exactly once")
    return tuple(s)

start = read_state("Enter initial state (0 = blank):")
goal = read_state("Enter goal state (0 = blank):")
astar(start, goal)
