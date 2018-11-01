
# N queens problem with backtracking

N = 8
a = []


def create_matrix(matrix_name, length):
    for i in range(length):
        matrix_name.append([0] * length)


def print_matrix(matrix_name, length):
    for i in range(length):
            print(matrix_name[i])


def can_place(matrix_name, x, y):
    # column_conflict

    for i in range(x):
        if matrix_name[i][y] == 1:
            return False

    # diagonal_conflict
    n = 1
    while x - n >= 0 and y - n >= 0:
        if matrix_name[x - n][y - n] == 1:
            return False
        n += 1

    m = 1
    while x - m >= 0 and y + m <= N - 1:
        if matrix_name[x - m][y + m] == 1:
            return False
        m += 1
    return True


def solution(matrix_name, row, length):
    if row >= length:
        return True

    for i in range(length):
        if can_place(matrix_name, row, i):
            matrix_name[row][i] = 1
            if solution(matrix_name, row + 1, length):
                return True
            matrix_name[row][i] = 0
    return False
