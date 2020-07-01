# create matrix of n*n
def n_queen_problem(n):
    board=[]
    for i in range(n):
        board.append([0]*n)
    def is_safe(row,column,n):
        for i in range(row):# check upside
            if board[i][column]==1:
                return 0
        r=row
        c=column
        while (r and c)>0: # check left upside
            r = r - 1
            c = c - 1
            if board[r][c]==1:
                return 0

        r=row
        c=column
        while (r>0) and (c<n-1):
            r = r - 1
            c = c = c + 1
            if board[r][c] == 1:
                return 0

        return 1

    def set_queen_in_row(row):
        if row ==n:
            return 1
        for column in range(n):

            if is_safe(row,column,n):
                board[row][column] = 1
                if set_queen_in_row(row+1):
                    return 1
                board[row][column]=0
    if set_queen_in_row(0):
        for i in range(n):
            print(board[i],"\n")
    else:
        print("no solution")

n_queen_problem(4)