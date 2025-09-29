from vector import Vector
from matrix import Matrix

if __name__ == "__main__":
    # vectors
    u = Vector([2., 3.])
    v = Vector([5., 7.])
    u.add(v)
    print(u) # Vector([7.0, 10.0])

    w = u + v
    print(w) # Vector([12.0, 17.0])
    print(u) # Vector([7.0, 10.0]), u is unchanged

    print("")

    u = Vector([2., 3.])
    v = Vector([5., 7.])
    u.sub(v)
    print(u) # Vector([-3.0, -4.0])

    w = u - v
    print(w) # Vector([-8.0, -11.0])
    print(u) # Vector([-3.0, -4.0], u is unchanged

    print("")

    u = Vector([2., 3.])
    u.scl(2.)
    print(u) # Vector([4.0, 6.0])

    w = 2. * u
    print(w) # Vector([8.0, 12.0])
    print(u) # Vector([4.0, 6.0]), u is unchanged

    print("")

    # matrices
    m = Matrix([[1., 2.],
                [3., 4.]])
    n = Matrix([[ 7., 4.],
                [-2., 2.]])
    m.add(n)
    print(m)
    # Matrix([[8.0, 6.0],
    #         [1.0, 6.0]])

    l = m + n
    print(l)
    # Matrix([[15.0, 10.0],
    #         [-1.0, 8.0]])

    print(m)
    # Matrix([[8.0, 6.0],
    #         [1.0, 6.0]]),  m is unchanged

    print("")

    m = Matrix([[1., 2.],
                [3., 4.]])
    n = Matrix([[ 7., 4.],
                [-2., 2.]])
    m.sub(n)
    print(m)
    # Matrix([[-6.0, -2.0],
    #         [ 5.0,  2.0]])

    l = m - n
    print(l)
    # Matrix([[-13.0, -6.0],
    #         [  7.0,  0.0]])
    print(m)
    # Matrix([[-6.0, -2.0],
    #         [ 5.0,  2.0]]), m is unchanged

    print("")

    m = Matrix([[1., 2.],
                [3., 4.]])
    m.scl(2.)
    print(m)
    # Matrix([[2.0, 4.0],
    #         [6.0, 8.0]])
    l = 2. * m
    print(l)
    # Matrix([[4.0, 8.0],
    #         [12.0, 16.0]])
    print(m)
    # Matrix([[2.0, 4.0],
    #         [6.0, 8.0]]), m is unchanged

    print("\n=== Tests from correction ===\n")

    print("=== Add ===")

    print(Vector([0, 0]) + Vector([0, 0]))
    print(Vector([1, 0]) + Vector([0, 1]))
    print(Vector([1, 1]) + Vector([1, 1]))
    print(Vector([21, 21]) + Vector([21, 21]))
    print(Vector([-21, 21]) + Vector([21, -21]))
    print(Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) + Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

    print("")
    print(Matrix([[0, 0], [0, 0]]) + Matrix([[0, 0], [0, 0]]))
    print(Matrix([[1, 0], [0, 1]]) + Matrix([[0, 0], [0, 0]]))
    print(Matrix([[1, 1], [1, 1]]) + Matrix([[1, 1], [1, 1]]))
    print(Matrix([[21, 21], [21, 21]]) + Matrix([[21, 21], [21, 21]]))

    print("\n=== Substract ===")
    print(Vector([0, 0]) - Vector([0, 0]))
    print(Vector([1, 0]) - Vector([0, 1]))
    print(Vector([1, 1]) - Vector([1, 1]))
    print(Vector([21, 21]) - Vector([21, 21]))
    print(Vector([-21, 21]) - Vector([21, -21]))
    print(Vector([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) - Vector([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))

    print("")
    print(Matrix([[0, 0], [0, 0]]) - Matrix([[0, 0], [0, 0]]))
    print(Matrix([[1, 0], [0, 1]]) - Matrix([[0, 0], [0, 0]]))
    print(Matrix([[1, 1], [1, 1]]) - Matrix([[1, 1], [1, 1]]))
    print(Matrix([[21, 21], [21, 21]]) - Matrix([[21, 21], [21, 21]]))

    print("\n=== Scalar Multiply ===")
    print(1 * Vector([0, 0]))
    print(1 * Vector([1, 0]))
    print(2 * Vector([1, 1]))
    print(Vector([21, 21]) * 2)
    print(Vector([42, 42]) * 0.5)

    print("")
    print(0 * Matrix([[0, 0], [0, 0]]))
    print(1 * Matrix([[1, 0], [0, 1]]))
    print(Matrix([[1, 2], [3, 4]]) * 2)
    print(Matrix([[21, 21], [21, 21]]) * 0.5)

