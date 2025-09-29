from vector import Vector
from linear_combination import linear_combination

if __name__ == "__main__":
    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])
    print("Example 1: ", linear_combination([e1, e2, e3], [10., -2., 0.5]))
    #              Vector([10.0, -2.0, 0.5])

    v1 = Vector([1.,  2.,   3.])
    v2 = Vector([0., 10., -100.])
    print("Example 2: ", linear_combination([v1, v2], [10., -2.]))
    #              Vector([10.0, 0.0, 230.0])

    print("\n=== Tests from correction ===\n")

    print(linear_combination([Vector([-42., 42.])], [-1.]))
    print(linear_combination([Vector([-42]), Vector([-42]), Vector([-42])], [-1., 1., 0.]))
    print(linear_combination([Vector([-42, 42.]), Vector([1., 3.]), Vector([10., 20.])], [1., -10., -1.]))
    print(linear_combination([Vector([-42, 100., -69.5]), Vector([1., 3., 5.])], [1., -10.]))