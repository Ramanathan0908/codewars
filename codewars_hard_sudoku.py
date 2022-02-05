board = [[0, 0, 5, 0, 0, 0, 8, 0, 0], [0, 2, 0, 8, 0, 9, 0, 7, 0], [3, 0, 0, 0, 4, 0, 0, 0, 1], [0, 3, 0, 2, 0, 6, 0, 1, 0], [0, 0, 2, 0, 0, 0, 5, 0, 0], [0, 7, 0, 5, 0, 4, 0, 6, 0], [2, 0, 0, 0, 6, 0, 0, 0, 4], [0, 8, 0, 4, 0, 2, 0, 9, 0], [0, 0, 7, 0, 0, 0, 2, 0, 0]]


def solve(board):
    new_board = []
    rows = [[False for j in range(9)] for i in range(9)]
    cols = [[False for j in range(9)] for i in range(9)]
    sqrs = [[False for j in range(9)] for i in range(9)]

    for i in range(9):
        for j in range(9):
            new_board.append(board[i][j])
            if board[i][j] != 0:
                rows[i][board[i][j] - 1] = True
                cols[j][board[i][j] - 1] = True
                sqrs[(i // 3) * 3 + j // 3][board[i][j] - 1] = True


    def solved(bo):
        try:
            k = bo.index(0)

            i = (k) // 9
            j = (k) % 9
            sqr = (i // 3) * 3 + j // 3

            for num in range(9):
                if not rows[i][num] and not cols[j][num] and not sqrs[sqr][num]:
                    bo[k]= num + 1
                    rows[i][num] = True
                    cols[j][num] = True
                    sqrs[sqr][num] = True

                    if solved(bo):
                        return True
                    bo[k]= 0
                    rows[i][num] = False
                    cols[j][num] = False
                    sqrs[sqr][num] = False

        except ValueError:
            return True

        return False

    solved(new_board)
    sol_board = [[0 for j in range(9)] for i in range(9)]
    for i in range(81):
        sol_board[i // 9][i % 9] = new_board[i]
    return sol_board

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

print_board(solve(board))



