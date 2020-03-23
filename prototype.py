# python3


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 6, end="")
            print("+", end="")
            print("-" * 7, end="")
            print("+", end="")
            print("-" * 6,)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")

            if j == 8:
                print("")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j       # return ROW, col
    return None


def valid(board, num, pos):
    row, col = pos
    for i in range(len(board)):
        if board[i][col] == num and i != row:
            return False
    for j in range(len(board[0])):
        if board[row][j] == num  and j != col:
            return False
    # square check:
    row_st = row // 3 * 3
    col_st = col // 3 * 3
    for i in range(row_st, row_st+3):
        for j in range(col_st, col_st+3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


# 1. pick an empty square (in a row)
# 2. try all numbers, until one is found that works
# 3. repeat
# 4. backtrack, if necessary
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True
            board[row][col] = 0

    return False


if __name__ == '__main__':
    input_board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    print_board(input_board)
    print("=" * 25)
    solve(input_board)
    print_board(input_board)
