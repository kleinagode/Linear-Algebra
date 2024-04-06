def extended_vector(vec):    #this will turn any vector with less than 3 components into a 3-vector
    vec.append(0)
    return vec

def cross_product(vec1,vec2):

    if len(vec1) > 1 and len(vec1) < 3:
        vec1 = extended_vector(vec1)

    if len(vec2) > 1 and len(vec2) < 3:
        vec2 = extended_vector(vec2)

    if len(vec1) == len(vec2):
        element_1 = (vec1[1] * vec2[2]) - (vec1[2] * vec2[1])
        element_2 = (vec1[2] * vec2[0]) - (vec1[0] * vec2[2])
        element_3 = (vec1[0] * vec2[1]) - (vec1[1] * vec2[0])

        cp = [element_1, element_2, element_3]
        return cp    
    else:
        return "Please enter 2D or 3D vectors."                                      

if __name__ == "__main__":
    inpvec1 = input()  # reads in a vector
    vector1 = [float(t.strip("[](), ")) for t in inpvec1.split(",")]  # creates a list for the first vector

    inpvec2 = input()  # reads in a vector
    vector2 = [float(t.strip("[](), ")) for t in inpvec2.split(",")]  # creates a list for the second vector

    print(cross_product(vector1,vector2))