from matrix import Matrix
from determinant import determinant

if __name__ == "__main__":
    tests = [
        Matrix([[1., -1.], [-1., 1.]]), #0.0
        Matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]]), # 8.0
        Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]]),  # -174.0
        Matrix([[8., 5., -2., 4.], [4., 2.5, 20., 4.], [8., 5., 1., 4.], [28., -4., 17., 1.]])  # 1032.0
    ]
    for M in tests:
        print("det(")
        print(M)
        print(") =", determinant(M), "\n")