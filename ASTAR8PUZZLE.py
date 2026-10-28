
import heapq

def manhattan(state, goal):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile == 0:
            continue

        j = goal.index(tile)

        distance += abs(i // 3 - j // 3)
        distance += abs(i % 3 - j % 3)

    return distance


def solve_astar(start, goal):
    pq = []
    heapq.heappush(pq, (manhattan(start, goal), 0, start))

    parent = {start: None}
    cost = {start: 0}

    while pq:
        f, g, state = heapq.heappop(pq)

        if state == goal:
            path = []

            while state is not None:
                path.append(state)
                state = parent[state]

            path.reverse()

            print("\nSolution found!")
            print("Number of moves:", len(path) - 1)

            for state in path:
                for i in range(0, 9, 3):
                    print(state[i:i + 3])
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
            new_state = list(state)
            new_state[zero], new_state[pos] = (
                new_state[pos], new_state[zero]
            )
            new_state = tuple(new_state)

            new_g = g + 1

            if new_g < cost.get(new_state, float("inf")):
                cost[new_state] = new_g
                parent[new_state] = state

                h = manhattan(new_state, goal)
                heapq.heappush(pq, (new_g + h, new_g, new_state))

    print("No solution found.")


def read_state(message):
    print(message)
    state = []

    for i in range(3):
        state.extend(map(int, input().split()))

    if sorted(state) != list(range(9)):
        raise ValueError("Enter each number from 0 to 8 exactly once.")

    return tuple(state)


start = read_state("Enter initial state (0 represents blank):")
goal = read_state("Enter goal state (0 represents blank):")

solve_astar(start, goal)
