def solve(board, col, n, solutions):
    if col >= n:
        solutions.append([row[:] for row in board])
        return
    
    for i in range(n):
        if issafe(board, i, col, n):
            board[i][col] = 1
            solve(board, col + 1, n, solutions)
            board[i][col] = 0  # Backtrack

def issafe(board, row, col, n):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def printSolution(solutions, n):
    for sol in solutions:
        for i in range(n):
            for j in range(n):
                print(sol[i][j], end=" ")
            print()
        print()

def main():
    n = int(input("Enter number of queens to place: "))
    board = [[0] * n for _ in range(n)]
    solutions = []
    
    solve(board, 0, n, solutions)
    
    if solutions:
        print(f"Total {len(solutions)} solutions found for {n} queens:")
        printSolution(solutions, n)
    else:
        print("No solution found for", n, "queens")

if __name__ == "__main__":
    main()
