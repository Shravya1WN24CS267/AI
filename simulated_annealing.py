import random
import math

def heuristic(board):
    conflicts = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                conflicts += 1

            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def print_board(board):
    n = len(board)

    for row in range(n):
        for col in range(n):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


def simulated_annealing(n):
    board = list(range(n))
    random.shuffle(board)

    temperature = 100
    cooling_rate = 0.90
    step = 1

    print("Step 1: Initial Board")
    print_board(board)
    print("Heuristic:", heuristic(board))

    while temperature > 0.01:

        current_h = heuristic(board)

        if current_h == 0:
            print("\nSolution found!")
            return board

        new_board = board[:]

        col = random.randint(0, n - 1)
        row = random.randint(0, n - 1)

        new_board[col] = row

        new_h = heuristic(new_board)
        delta = new_h - current_h

        if delta < 0:
            board = new_board
            accepted = True

        elif random.random() < math.exp(-delta / temperature):
            board = new_board
            accepted = True

        else:
            accepted = False

        print(f"\nStep {step + 1}:")
        print("Temperature:", round(temperature, 2))
        print("New Heuristic:", new_h)
        print("Move accepted:", accepted)

        if accepted:
            print_board(board)
            print("Current Heuristic:", heuristic(board))

        temperature *= cooling_rate
        step += 1

        if heuristic(board) == 0:
            print("\nSolution found!")
            return board

    return None


n = int(input("Enter number of queens: "))

solution = simulated_annealing(n)

if solution:
    print("\nFinal Solution:")
    print_board(solution)
else:
    print("No solution found.")