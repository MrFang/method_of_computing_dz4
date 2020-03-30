def findMaxInColumn(column, matrix):
    max = abs(matrix[column][column])
    max_row = column
    for row in range(column, len(matrix)):
        if (abs(matrix[row][column]) > max):
            max = abs(matrix[row][column])
            max_row = row
    return max_row

def swapLines(x, y, matrix):
    temp = matrix[x]; matrix[x] = matrix[y]; matrix[y] = temp

    return matrix

def mult(num, row):
    r = list()
    for item in row:
        r.append(item * num)

    return r

def sum(row1, row2):
    result = list()
    for idx, item in enumerate(row1):
        result.append(row1[idx] + row2[idx])

    return result

def forwardPropagation(matrix, col):
    for column in range(0, len(matrix)):

        max_row = findMaxInColumn(column, matrix)

        matrix = swapLines(column, max_row, matrix)
        col = swapLines(column, max_row, col)

        col[column] = col[column] / matrix[column][column]
        matrix[column] = mult(1/matrix[column][column], matrix[column])

        for num in range(column + 1, len(matrix)):
            col[num] = col[num] + col[column] * -matrix[num][column]
            matrix[num] = sum(matrix[num], mult(-matrix[num][column], matrix[column]))

def backwardPropagation(matrix, col):
    for i in range(len(matrix)-1, 0, -1):
        for j in range(i-1, -1, -1):
            col[j] = col[j] + col[i]*-matrix[j][i]
            matrix[j] = sum(matrix[j], mult(-matrix[j][i], matrix[i]))

def findRoots(matrix, col):
    forwardPropagation(matrix, col)
    backwardPropagation(matrix, col)
    
    return col