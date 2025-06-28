from matrix import Matrix
from trace import trace

if __name__ == "__main__":
    A = Matrix([[1., 0.], [0., 1.]])
    print("Tr A =", trace(A)) # 2.0

    print("")

    B = Matrix([[2., -5., 0.],
                [4.,  3., 7.],
                [-2., 3., 4.]])
    print("Tr B =", trace(B)) # 9.0

    print("")

    C = Matrix([[-2., -8., 4.],
                [ 1., -23., 4.],
                [ 0.,  6., 4.]])
    print("Tr C =", trace(C)) # -21.0