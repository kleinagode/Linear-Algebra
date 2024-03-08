inp1 = input()       # reads in the first matrix
inp1_strip = inp1.strip("(),[] ")              # removes brackets or parantheses and spaces
matrix1 = [
    list(map(float, t.split(","))) for t in inp1_strip.split(";")]    # creates a matrix for input

inp2 = input()       # reads in the second matrix
inp2_strip = inp2.strip("(),[] ")              # removes brackets or parantheses and spaces
matrix2 = [list(map(float, t.split(","))) for t in inp2_strip.split(";")]    # creates a matrix for input

def row_times_column(row,col):
    result = 0
    length = len(row)
    for i in range(length):
        result += row[i] * col[i]
    return result

def matrix_multiplication(mat1,mat2):
    Rows_1 = len(mat1)
    Cols_1 = len(mat1[0])
    Rows_2 = len(mat2)
    Cols_2 = len(mat2[0])
    
    if Cols_1 != Rows_2:
        return "Undefined as the number of columns in the first matrix does not equal the number of rows in the second matrix."
    
    product_matrix = [[0 for _ in range(Cols_2)] for _ in range(Rows_1)]
    
    for i in range(Rows_1):
        for j in range(Cols_2):
            column = [mat2[k][j] for k in range(Rows_2)]
            product_matrix[i][j] = row_times_column(mat1[i], column)
    
    return product_matrix

to_print = matrix_multiplication(matrix1,matrix2)

if isinstance(to_print, str):
    print(to_print)
else:
    for r in to_print:
        print(r)
