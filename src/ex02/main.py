from vector import Vector
from matrix import Matrix
from linear_interpolation import lerp

if __name__ == "__main__":
    # scalars
    print("scalar 0: ", lerp(0.0, 1.0, 0.0)) # 0.0
    print("scalar 1: ", lerp(0.0, 1.0, 1.0)) # 1.0
    print("scalar 1/2: ", lerp(0.0, 1.0, 0.5)) # 0.5
    print("scalar .3: ", lerp(21.0, 42.0, 0.3)) # 27.3

    print("")

    # vectors
    v1 = Vector([2., 1.])
    v2 = Vector([4., 2.])
    print("vector .3:", lerp(v1, v2, 0.3)) # [2.6, 1.3]

    print("")

    # matrices
    m1 = Matrix([[2., 1.], [3., 4.]])
    m2 = Matrix([[20., 10.], [30., 40.]])
    print("matrix .5:", lerp(m1, m2, 0.5))
    # Matrix([[11.0, 5.5],
    #         [16.5, 22.0]])