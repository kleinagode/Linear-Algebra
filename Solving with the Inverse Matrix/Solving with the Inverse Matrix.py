def extend_matrix(mat):
    n = len(mat)
    for i in range(n):
        mat[i].extend([0] * i + [1] + [0] * (n - i - 1))
    return mat

def matrix_minor(mat, i, j):
    return [row[:j] + row[j+1:] for row in (mat[:i] + mat[i+1:])]

def matrix_determinant(mat):
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    determinant = 0
    for c in range(len(mat)):
        determinant += ((-1) ** c) * mat[0][c] * matrix_determinant(matrix_minor(mat, 0, c))
    return determinant

def matrix_transpose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

def matrix_inverse(mat):
    if len(mat) != len(mat[0]):
        return "There is no inverse matrix as this matrix is not square."
    determinant = matrix_determinant(mat)
    if determinant == 0:
        return "The matrix is square but it is not invertible."
    if len(mat) == 2:
        return [[mat[1][1] / determinant, -1 * mat[0][1] / determinant],
                [-1 * mat[1][0] / determinant, mat[0][0] / determinant]]
    cofactors = []
    for r in range(len(mat)):
        cofactor_row = []
        for c in range(len(mat)):
            minor = matrix_minor(mat, r, c)
            cofactor_row.append(((-1) ** (r + c)) * matrix_determinant(minor))
        cofactors.append(cofactor_row)
    cofactors = matrix_transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors

def matrix_vector_multiply(matrix, vector):
    result = []
    for row in matrix:
        total = sum([a * b for a, b in zip(row, vector)])
        result.append(total)
    return result

def solve_system(matrix, vector):
    inverse = matrix_inverse(matrix)
    if isinstance(inverse, str):
        return inverse
    elif len(matrix) != len(vector):
        return "The system is not solvable as the matrix and vector are not the right size."
    else:
        result = matrix_vector_multiply(inverse, vector)
        return result

# Read input matrices
inp = input()
inp_strip = inp.strip("(),[] ")
matrix = [list(map(float, t.split(","))) for t in inp_strip.split(";")]

inp_vec = input()
inp_vec_strip = inp_vec.strip("(),[] ")
vector = [float(t) for t in inp_vec_strip.split(";")]

# Solve the system of equations
to_print = solve_system(matrix, vector)

# Print the result
if isinstance(to_print, str):
    print(to_print)
else:
    for i, val in enumerate(to_print):
        print("x_{} = {:.3f}".format(i+1, val))
