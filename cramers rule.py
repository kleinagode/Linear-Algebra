def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        det = 0
        for j in range(n):
            minor = [row[:j] + row[j+1:] for row in matrix[1:]]
            det += (-1)**j * matrix[0][j] * determinant(minor)
        return det

def cramers_rule(mat, b):
    n = len(mat)
    if n != len(mat[0]):
        return "Please enter a square matrix."
    if n != len(b):
        return "This can not be solved as the vector is not the right size."
    det_A = determinant(mat)
    if det_A == 0:
        return "The system does not have a unique solution because the determinant is zero."
    solutions = []
    for i in range(n):
        temp_mat = [row[:] for row in mat]  # Make a copy of mat
        for j in range(n):
            temp_mat[j][i] = b[j]  # Replace the ith column with the vector
        det_temp = determinant(temp_mat)
        x_i = det_temp / det_A
        solutions.append(x_i)
    return solutions

if __name__ == "__main__":
    inp = input()  # reads in the matrix
    inp_strip = inp.strip("(),[] ")  # removes brackets or parantheses and spaces
    matrix = [list(map(float, t.split(","))) for t in inp_strip.split(";")]  # creates a matrix for input

    inp2 = input()  # reads in the second matrix
    inpvec = inp2.strip("(),[] ")  # removes brackets or parantheses and spaces
    vector = [float(t.strip("; ")) for t in inpvec.split(";")]    # creates a list for the b vector

    result = cramers_rule(matrix, vector)
    if isinstance(result, str):
        print(result)
    else:
        for i, solution in enumerate(result):
            print(f"x_{i+1} = {solution:.3f}")
