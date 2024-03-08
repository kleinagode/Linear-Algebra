def under_nonzero_finder(mat, m, k):
    first_nonzero_loc = len(mat) + 1
    for n in range(k, len(mat)):
        if mat[n][m] != 0:
            first_nonzero_loc = n
            break
    return first_nonzero_loc

def subtract_row_times_num_to_row(first_row, sec_row, a):
    for k in range(len(first_row)):
        sec_row[k] = sec_row[k] - a * first_row[k]
    return sec_row
    
def mult_row_by_num(row, a):
    for k in range(len(row)):
        row[k] *= a
    return row

def reduced_echelon_calculator(mat):
    R = len(mat)
    C = len(mat[0])
    
    i = 0
    j = 0
    while j < C:
        zero_location = under_nonzero_finder(mat, j, i)
        if zero_location == R + 1:
            j += 1
        elif zero_location > i:
            temp_row = mat[zero_location]
            mat[zero_location] = mat[i]
            mat[i] = temp_row
        else:
            a = mat[i][j]
            mat[i] = mult_row_by_num(mat[i], 1/a)
            for l in range(i + 1, R):
                a = mat[l][j]
                mat[l] = subtract_row_times_num_to_row(mat[i], mat[l], a)
            for l in range(i):
                a = mat[l][j]
                mat[l] = subtract_row_times_num_to_row(mat[i], mat[l], a)
            j += 1
            i += 1
    return mat

def make_extended_matrix(mat):
    R = len(mat)
    C = len(mat[0])
    
    for m in range(R):
        mat[m] = mat[m] + [1.0 if i == m else 0.0 for i in range(R)]
        
    return mat

def inverse_calculator(mat):
    C = len(mat[0])
    R = len(mat)
    
    if R != C:
        return "There is no inverse matrix as this matrix is not square."
    else:
        extended_matrix = make_extended_matrix(mat)
        reduced_extended_matrix = reduced_echelon_calculator(extended_matrix)
        
        for i in range(R):
            pivot = reduced_extended_matrix[i][i]
            if pivot == 0:
                return "The matrix is square but it is not invertible."
        
        inverse = [[reduced_extended_matrix[i][j] for j in range(C, 2 * C)] for i in range(R)]
        return inverse

inp = input()
inp_strip = inp.strip("(),[] ")  
matrix = [list(map(float, t.split(","))) for t in inp_strip.split(";")]

simplified = inverse_calculator(matrix)

if type(simplified) == str:
    print(simplified)
else:
    for r in simplified:
        print(r)
