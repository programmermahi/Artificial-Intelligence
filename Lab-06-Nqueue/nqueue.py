def solve(board, col, n):
    if col >= n:
        return True
    
    for i in range(n):
        if issafe(board, i, col, n):
            board[i][col] = 1
            if solve(board, col + 1, n):
                return True
            board[i][col] = 0  # Backtrack
    
    return False

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

def printSolution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

def main():
    n = int(input("Enter number of queens to place: "))
    board = [[0] * n for _ in range(n)]
    
    if solve(board, 0, n):
        print("Solution exists")
        printSolution(board, n)
    else:
        print("No solution found for", n, "queens")

if __name__ == "__main__":
    main()
