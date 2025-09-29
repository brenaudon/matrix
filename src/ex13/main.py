from matrix import Matrix
from rank import rank

if __name__ == "__main__":
    tests = [
        Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]),
        Matrix([[1., 2., 0., 0.], [2., 4., 0., 0.], [-1., 2., 1., 1.]]),
        Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.], [21., 18., 7.]])
    ]
    for M in tests:
        print("M =\n", M)
        print("rank(M) =", rank(M))
        print("")

    print("\n=== Tests from correction ===\n")

    print(rank(Matrix([[0, 0], [0, 0]])))
    print(rank(Matrix([[1, 0], [0, 1]])))
    print(rank(Matrix([[2, 0], [0, 2]])))
    print(rank(Matrix([[1, 1], [1, 1]])))
    print(rank(Matrix([[0, 1], [1, 0]])))
    print(rank(Matrix([[1, 2], [3, 4]])))
    print(rank(Matrix([[-7, 5], [4, 6]])))
    print(rank(Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])))