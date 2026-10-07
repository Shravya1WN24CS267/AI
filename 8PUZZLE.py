
def get_moves(state):

    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    moves = []

    # Move Up
    if row > 0:
        moves.append(zero - 3)

    # Move Down
    if row < 2:
        moves.append(zero + 3)

    # Move Left
    if col > 0:
        moves.append(zero - 1)

    # Move Right
    if col < 2:
        moves.append(zero + 1)

    return moves




    zero = state.index(0)

    new_state = list(state)

    # Swap blank with new position
    new_state[zero], new_state[new_zero] = \
        new_state[new_zero], new_state[zero]

    return tuple(new_state)



def depth_limited_dfs(state, goal, depth, path):

    # Goal found
    if state == goal:
        return path

    # Depth limit reached
    if depth == 0:
        return None

    # Try all possible moves
    for new_zero in get_moves(state):

        new_state = make_move(state, new_zero)

        # Avoid states already present in current path
        if new_state not in path:

            result = depth_limited_dfs(
                new_state,
                goal,
                depth - 1,
                path + [new_state]
            )

            # Solution found
            if result is not None:
                return result

    return None



def ids(start, goal):

    depth = 0

    while True:

        print("Searching at depth:", depth)

        solution = depth_limited_dfs(
            start,
            goal,
            depth,
            [start]
        )

        # Goal found
        if solution is not None:

            print("\n================================")
            print("       GOAL FOUND")
            print("================================")

            print("Answer depth:", depth)
            print("Number of moves:", len(solution) - 1)

            return solution, depth

        # Increase depth
        depth += 1



def display_state(state):

    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])



def display_solution(solution):

    print("\n================================")
    print("          SOLUTION")
    print("================================")

    for i, state in enumerate(solution):

        print("\nStep", i)
        print("-------")

        display_state(state)




print("================================")
print("     8 PUZZLE USING IDS")
print("================================")

print("\nEnter Initial State")
print("Use 0 for blank space.")
print("Enter 9 numbers separated by spaces.")

start = tuple(
    map(int, input("Enter 9 numbers: ").split())
)


print("\nEnter Goal State")

goal = tuple(
    map(int, input("Enter 9 numbers: ").split())
)



solution, answer_depth = ids(
    start,
    goal
)
display_solution(solution)
