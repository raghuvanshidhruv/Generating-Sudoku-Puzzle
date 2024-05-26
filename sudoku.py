import random

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid(board, num, row, col):
    # Check if 'num' is not present in the current row, column, and 3x3 grid
    return (
        all(num != board[row][j] for j in range(9)) and
        all(num != board[i][col] for i in range(9)) and
        all(num != board[i][j] for i in range(row - row % 3, row - row % 3 + 3) for j in range(col - col % 3, col - col % 3 + 3))
    )

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, num, row, col):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack if the solution is not valid
                return False
    return True  # The board is solved

def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    solve_sudoku(board)

    # Remove some numbers to create the puzzle
    for _ in range(random.randint(30, 50)):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        board[row][col] = 0

    return board

# Example Usage
sudoku_board = generate_sudoku()
print("Generated Sudoku Puzzle:")
print_board(sudoku_board)
