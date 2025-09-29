from vector import Vector
from matrix import Matrix
from mul_mat import mat_vec_mul, mat_mat_mul

if __name__ == "__main__":
    # Matrix · vector
    A = Matrix([[1., 0.], [0., 1.]])
    u = Vector([4., 2.])
    print("A·u = ", mat_vec_mul(A, u)) # [4., 2.]

    print("")

    B = Matrix([[2., 0.], [0., 2.]])
    print("B·u = ", mat_vec_mul(B, u)) # [8., 4.]

    print("")

    C = Matrix([[2., -2.], [-2., 2.]])
    print("C·u = ", mat_vec_mul(C, u)) # [4., -4.]

    print("")

    # Matrix · matrix
    I = Matrix([[1., 0.], [0., 1.]])
    print("I·I = ", mat_mat_mul(I, I)) # Identity

    print("")

    D = Matrix([[2., 1.], [4., 2.]])
    print("I·D = ", mat_mat_mul(I, D)) # [2., 1.], [4., 2.]

    print("")

    E = Matrix([[3., -5.], [6., 8.]])
    F = Matrix([[2.,  1.], [4.,  2.]])
    print("E·F = ", mat_mat_mul(E, F)) # [-14., -7.], [44.,  22.]

    print("\n=== Tests from correction ===\n")

    print(mat_vec_mul(Matrix([[0, 0], [0, 0]]), Vector([7, 8])))
    print(mat_vec_mul(Matrix([[1, 0], [0, 1]]), Vector([5, 6])))
    print(mat_vec_mul(Matrix([[1, 1], [1, 1]]), Vector([4, 2])))
    print(mat_vec_mul(Matrix([[2, 0], [0, 2]]), Vector([2, 1])))
    print(mat_vec_mul(Matrix([[0.5, 0], [0, 0.5]]), Vector([4, 2])))