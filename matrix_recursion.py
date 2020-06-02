def spiral(no_of_rounds_completed, vertical_iteration, horizontal_iteration, matrix):
    no_of_columns = n = len(matrix[0])
    no_of_rows = m = len(matrix)
    no_of_rounds = min(no_of_columns,no_of_rows) - min(no_of_columns,no_of_rows)//2
    i=no_of_rounds_completed
    if horizontal_iteration<n:
        for z in range(i,no_of_columns-i):                      #left to right
            print(matrix[i][z])
        horizontal_iteration = horizontal_iteration + 1
    else:return
    if vertical_iteration<no_of_rows-1:
        for k in range(i + 1, no_of_rows - i):                  #top to down
            print(matrix[k][ no_of_columns - i - 1])
        vertical_iteration= vertical_iteration + 1
    else:return
    if horizontal_iteration < n:
        for j in reversed(range(i, no_of_columns - 1 - i)):     #right to left
            print(matrix[no_of_rows - i - 1][j])
        horizontal_iteration= horizontal_iteration + 1
    else:return
    if vertical_iteration < no_of_rows-1:
        for k in reversed(range(i + 1, no_of_rows - 1 - i)):    #down to up
            print(matrix[k][i])
        vertical_iteration = vertical_iteration + 1
    else:return
    i = i + 1    # 1 round completed
    if i < no_of_rounds:
        spiral(i, vertical_iteration, horizontal_iteration, matrix)




matrix_1=[[ 1, 2, 3, 4, 5, 6,49],
        [ 7, 8, 9,10,11,12,50],
        [13,14,15,16,17,18,51],
        [19,20,21,22,23,24,52],
        [25,26,27,28,29,30,53],
        [31,32,33,34,35,36,54],
        [37,38,39,40,41,42,55],
        [43,44,45,46,47,48,56]]
#spiral(0,0,0,matrix_1)

matrix_2=[[ 1, 2, 3, 4, 5, 6],
          [ 7, 8, 9,10,11,12],
          [13,14,15,16,17,18],
          [19,20,21,22,23,24],
          [25,26,27,28,29,30],
          [31,32,33,34,35,36],
          [37,38,39,40,41,42],
          [43,44,45,46,47,48]]
#spiral(0,0,0,matrix_2)

matrix_3=[[1,2,3,4,5,6,7,8,9],
          [10,11,12,13,14,15,16,17,18]]
#spiral(0,0,0,matrix_3)

matrix_4=[[1,2],
          [3,4],
          [5,6],
          [7,8],
          [9,10]]
#spiral(0,0,0,matrix_4)

matrix_5=[[1,2],
          [3,4]]
#spiral(0,0,0,matrix_5)

matrix_6=[[ 1, 2, 3, 4, 5, 6],
          [ 7, 8, 9,10,11,12],
          [13,14,15,16,17,18],
          [19,20,21,22,23,24],
          [25,26,27,28,29,30],
          [31,32,33,34,35,36]]
#spiral(0,0,0,matrix_6)

matrix_7=[[1],[2],[3],[4]]
#spiral(0,0,0,matrix_7)
matrix=[[1,2,3,4,5,6]]
#spiral(0,0,0,matrix)
matrix=[[1]]
#spiral(0,0,0,matrix)
matrix=[[ 1, 2, 3, 4, 5, 6,49],
        [ 7, 8, 9,10,11,12,50],
        [13,14,15,16,17,18,51],]
#spiral(0,0,0,matrix)