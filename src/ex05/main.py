from vector import Vector
from cosine import angle_cos

if __name__ == "__main__":
    u = Vector([1., 0.])
    v = Vector([1., 0.])
    print("0°: ", angle_cos(u, v))  # 1.0

    print("")

    u = Vector([1., 0.])
    v = Vector([0., 1.])
    print("90°: ", angle_cos(u, v)) # 0.0

    print("")

    u = Vector([-1., 1.])
    v = Vector([ 1., -1.])
    print(f"180°: {angle_cos(u, v):.6f}") # -1.0, .6f to format to 6 decimal places and avoid rounding errors

    print("")

    u = Vector([2., 1.])
    v = Vector([4., 2.])
    print(f"0°: {angle_cos(u, v):.6f}")  # 1.0

    print("")

    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(angle_cos(u, v)) # 0.974631846

    print("\n=== Tests from correction ===\n")

    print(angle_cos(Vector([1, 0]), Vector([0, 1])))
    print(angle_cos(Vector([8, 7]), Vector([3, 2])))
    print(angle_cos(Vector([1, 1]), Vector([1, 1])))
    print(angle_cos(Vector([4, 2]), Vector([1, 1])))
    print(angle_cos(Vector([-7, 3]), Vector([6, 4])))
