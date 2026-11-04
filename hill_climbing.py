import random

def calculate_heuristic(board):
    conflicts = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):

            # Same row
            if board[i] == board[j]:
                conflicts += 1

            # Same diagonal
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def hill_climbing(n):
    # Random initial state
    board = [random.randint(0, n - 1) for _ in range(n)]

    while True:
        current_h = calculate_heuristic(board)

        # Goal state
        if current_h == 0:
            return board

        best_board = board[:]
        best_h = current_h

        # Generate neighboring states
        for col in range(n):
            for row in range(n):

                new_board = board[:]
                new_board[col] = row

                h = calculate_heuristic(new_board)

                if h < best_h:
                    best_h = h
                    best_board = new_board

        # No better neighbor found
        if best_h >= current_h:
            return None

        board = best_board


def print_board(board):
    n = len(board)

    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Main program
n = int(input("Enter number of queens: "))

solution = hill_climbing(n)

if solution:
    print("Solution found:")
    print_board(solution)
else:
    print("Local optimum reached. No solution found.")