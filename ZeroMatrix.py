# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to O.

A = []


def create_matrix(matrix, row, col):
    for i in range(row):
        matrix.append([1] * col)


def print_matrix(matrix):
    for i in range(len(matrix)):
            print(matrix[i])


# Time complexity: O(M X N)
# Space complexity: O(M + N)
def set_zeros(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    row = [0] * row_len
    col = [0] * col_len
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1

    for i in range(row_len):
        for j in range(col_len):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0


# Time complexity: O(M X N)
# Space complexity: O(1)
def change_zero(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    first_row = 0
    first_col = 0

    for i in range(col_len):
        if matrix[0][i] == 0:
            first_row = 1

    for i in range(row_len):
        if matrix[i][0] == 0:
            first_col = 1
            

#     if row_len == 1 or col_len == 1:
#         if first_row == 1 and row_len == 1:
#             for i in range(col_len):
#                 matrix[0][i] = 0
#             return
#         elif first_col == 1 and col_len == 1:
#             for i in range(row_len):
#                 matrix[i][0] = 0
#             return
#         else:
#             return


    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, row_len):
        for j in range(1, col_len):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_col == 1:
        for i in range(row_len):
            matrix[i][0] = 0

    if first_row == 1:
        for i in range(col_len):
            matrix[0][i] = 0
