from matrix import Matrix
from inverse import inverse
from mul_mat import mat_mat_mul

if __name__ == "__main__":
    tests = [
        Matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]]),
        Matrix([[2., 0., 0.], [0., 2., 0.], [0., 0., 2.]]),
        Matrix([[8., 5., -2.], [4., 7., 20.], [7., 6., 1.]])
    ]
    for M in tests:
        print("M =\n", M)
        invM = inverse(M)
        print("M⁻¹ =\n", invM)

        # quick check A·A⁻¹ ≈ I
        print("M·M⁻¹ =\n", mat_mat_mul(M, invM))

        print("")