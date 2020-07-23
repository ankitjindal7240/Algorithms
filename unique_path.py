rows =6
columns=9
matrix=[]
for i in range(rows):
    matrix.append([1]*columns)
# using recursion

def paths(row,column):
    if row ==1 or column ==1:
        return 1
    else:
        return paths(row-1,column) +paths(row,column-1)
p=paths(rows,columns)
print(p)

# using dp


def unique_paths(rows,columns):
    for row in range(1,rows):
        for column in range(1,columns):
            matrix[row][column]=matrix[row-1][column]+matrix[row][column-1]

    return matrix[rows-1][columns-1]
p=unique_paths(rows,columns)
print(p)