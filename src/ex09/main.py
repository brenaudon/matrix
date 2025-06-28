from matrix import Matrix
from transpose import transpose

if __name__ == "__main__":
    A = Matrix([[1., 2., 3.],
                [4., 5., 6.]])
    print("Aᵀ = ", transpose(A))

    print("")

    B = Matrix([[7.]])
    print("Bᵀ = ", transpose(B))