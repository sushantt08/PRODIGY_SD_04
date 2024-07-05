SIZE = 9

def is_valid(board, row, col, num):
    # Check if num is not in the current row and column
    for x in range(SIZE):
        if board[row][x] == num or board[x][col] == num:
            return False

    # Check if num is not in the current 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == 0:  # find an empty cell
                for num in range(1, SIZE + 1):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # reset on backtrack
                return False  # trigger backtracking
    return True  # puzzle solved

def print_board(board):
    for row in range(SIZE):
        for col in range(SIZE):
            print(board[row][col], end=" ")
        print()

def main():

    # Example unsolved Sudoku puzzle
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(board):
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
