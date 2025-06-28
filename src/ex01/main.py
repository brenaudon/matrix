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