def spiral(matrix):
    no_of_columns = n = len(matrix[0])
    no_of_rows = m = len(matrix)
    no_of_rounds = min(no_of_columns,no_of_rows) - min(no_of_columns,no_of_rows)//2
    no_of_rounds_completed = i = 0
    # if n or m ==1:                      #if there is only one row or one column
    #     print(matrix)
    #     return
    vertical_itration=0
    horizontal_itration=0
    while i < no_of_rounds:
        #print(matrix[i][i: no_of_columns - i])
        if horizontal_itration<n:
            for z in range(i,no_of_columns-i):                      #left to right
                print(matrix[i][z])                                 # we can avoid loop by  #print(matrix[i][i: no_of_columns - i])
            horizontal_itration=horizontal_itration+1
        else:return
        if vertical_itration<no_of_rows-1:
            for k in range(i + 1, no_of_rows - i):                  #top to down
                print(matrix[k][ no_of_columns - i - 1])
            vertical_itration=vertical_itration+1
        else:
            return
        if horizontal_itration < n:
            for j in reversed(range(i, no_of_columns - 1 - i)):     #right to left
                print(matrix[no_of_rows - i - 1][j])                #to avoid loop use print(matrix[no_of_rows - i - 1][ no_of_columns - 1 - i - 1:i-1:-1])
            horizontal_itration=horizontal_itration+1
        else:
            return
        if vertical_itration < no_of_rows-1:
            for k in reversed(range(i + 1, no_of_rows - 1 - i)):    #down to up
                print(matrix[k][i])
            vertical_itration = vertical_itration + 1
        else:
            return
        i = i + 1



matrix=[[1],[2],[3]]
#spiral(matrix)
matrix_1=[[ 1, 2, 3, 4, 5, 6,49],
        [ 7, 8, 9,10,11,12,50],
        [13,14,15,16,17,18,51],
        [19,20,21,22,23,24,52],
        [25,26,27,28,29,30,53],
        [31,32,33,34,35,36,54],
        [37,38,39,40,41,42,55],
        [43,44,45,46,47,48,56]]
spiral(matrix_1)

matrix_2=[[ 1, 2, 3, 4, 5, 6],
          [ 7, 8, 9,10,11,12],
          [13,14,15,16,17,18],
          [19,20,21,22,23,24],
          [25,26,27,28,29,30],
          [31,32,33,34,35,36],
          [37,38,39,40,41,42],
          [43,44,45,46,47,48]]
#spiral(matrix_2)

matrix_3=[[1,2,3,4,5,6,7,8,9],
          [10,11,12,13,14,15,16,17,18]]
#spiral(matrix_3)

matrix_4=[[1,2],
          [3,4],
          [5,6],
          [7,8],
          [9,10]]
#spiral(matrix_4)

matrix_5=[[1,2],
          [3,4]]
#spiral(matrix_5)

matrix_6=[[ 1, 2, 3, 4, 5, 6],
          [ 7, 8, 9,10,11,12],
          [13,14,15,16,17,18],
          [19,20,21,22,23,24],
          [25,26,27,28,29,30],
          [31,32,33,34,35,36]]
#spiral(matrix_6)

matrix_7=[[1],[2],[3],[4]]
#spiral(matrix_7)