def two_by_two_determinant(mat):   #calculates the determinant of a two by two matrix
   return (mat[0][0] * mat[1][1]) - (mat[0][1] * mat[1][0])

def eliminate_row_column(mat,col_to_remove):
    new_matrix = [[t for t in row ] for row in mat]    #creates a new temp matrix that is equal to mat
    
    new_matrix.remove(mat[0]) #removes the 0th row because I will always use a 0th row for leading  values

    for i in range(len(mat)-1):
        new_matrix[i].pop(col_to_remove)

    return new_matrix

def three_by_three_determinant(mat):
    leading_val = 0
    determinant = 0

    for i in range(len(mat)):
        leading_val = mat[0][i]
        col_to_remove = i
        
        temp_matrix = eliminate_row_column(mat,col_to_remove)
        temp_determinant = two_by_two_determinant(temp_matrix)

        determinant += (-1) ** i * leading_val * temp_determinant #We raise -1 to the power of i, if i is odd it will change the sign
    
    return determinant

if __name__ == "__main__":
    inp = input()  # reads in the matrix
    inp_strip = inp.strip("(),[] ")  # removes brackets or parantheses and spaces
    matrix = [list(map(float, t.split(","))) for t in inp_strip.split(";")]  # creates a matrix for input

    square = True

    for el in matrix: # Checks if the matrix is square
        if len(el) != len(matrix):
            square = False
    
    if not square:       # you will need an if statement to check that the matrix is square, if the size is 1, 2, 3, or something else. Each if statement will print a different result.
       print("Please enter a square matrix.")
    
    elif len(matrix) == 1:         #if it is size 1, print the element
        inp_strip = float(inp_strip)
        print(f"{inp_strip:.1f}")
    elif square and len(matrix) == 2:       #if it is size 2, print the result of the two_by_two_determinant
        print(two_by_two_determinant(matrix))
    elif len(matrix) == len(matrix[0]) and len(matrix) == 3:      #if it is size 3, print the result of the three_by_three_determinant
        print(three_by_three_determinant(matrix))
    else:
        print("We can only handle up to a 3 by 3 matrix. Sorry.")

 