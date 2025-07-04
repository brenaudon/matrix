from matrix import Matrix
from row_echelon import row_echelon

if __name__ == "__main__":
    examples = [
        Matrix([[1., 0., 0.],
                [0., 1., 0.],
                [0., 0., 1.]]),

        Matrix([[1., 2.],
                [3., 4.]]),

        Matrix([[1., 2.],
                [2., 4.]]),

        Matrix([[8., 5., -2., 4., 28.],
                [4., 2.5, 20., 4., -4.],
                [8., 5., 1., 4., 17.]]),
    ]

    for M in examples:
        print("Input:\n", M)
        print("Row‑echelon:\n", row_echelon(M), "\n")