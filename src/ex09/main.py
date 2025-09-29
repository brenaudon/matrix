from matrix import Matrix
from transpose import transpose

if __name__ == "__main__":
    A = Matrix([[1., 2., 3.],
                [4., 5., 6.]])
    print("Aᵀ = ", transpose(A))

    print("")

    B = Matrix([[7.]])
    print("Bᵀ = ", transpose(B))

    print("\n=== Tests from correction ===\n")

    print(transpose(Matrix([[0, 0], [0, 0]])))
    print(transpose(Matrix([[1, 0], [0, 1]])))
    print(transpose(Matrix([[1, 2], [3, 4]])))
    print(transpose(Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])))
    print(transpose(Matrix([[1, 2], [3, 4], [5, 6]])))