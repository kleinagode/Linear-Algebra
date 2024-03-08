inp1 = input()       # reads in the first matrix
inp1_strip = inp1.strip("(),[] ")              # removes brackets or parantheses and spaces
matrix1 = [list(map(float, t.split(","))) for t in inp1_strip.split(";")]    # creates a matrix for input

R_first = len(matrix1)       # number of rows for first matrix
C_first = len(matrix1[0])    # number of columns for first matrix

inp2 = input()       # reads in the second matrix
inp2_strip = inp2.strip("(),[] ")              # removes brackets or parantheses and spaces
matrix2 = [list(map(float, t.split(","))) for t in inp2_strip.split(";")]    # creates a matrix for input

R_second = len(matrix2)       # number of rows for second matrix
C_second = len(matrix2[0])    # number of columns for second matrix

# Verify that the matrices are the same size
if R_first != R_second or C_first != C_second:
    print("Undefined as the matrices are not the same size.")
else:
    matrix_sum = []
    for i in range(R_first):           # iterate through each row
        row_sum = []
        for j in range(C_first):       # iterate through each column
            element_sum = matrix1[i][j] + matrix2[i][j]  # sum of corresponding elements
            row_sum.append(element_sum)
        matrix_sum.append(row_sum)

    # Print the sum of matrices
    for row in matrix_sum:
        print(*row)
