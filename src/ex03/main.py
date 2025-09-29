from vector import Vector
from dot_product import dot

if __name__ == "__main__":
    examples = [
        (Vector([0., 0.]), Vector([1., 1.]), 0.0),
        (Vector([1., 1.]), Vector([1., 1.]), 2.0),
        (Vector([-1., 6.]), Vector([3., 2.]), 9.0),
    ]
    for u, v, ref in examples:
        result = dot(u, v)
        print(f"dot({u}, {v}) = {result}")
        assert abs(result - ref) < 1e-9

    print("\n=== Tests from correction ===\n")

    print(dot(Vector([0, 0]), Vector([0, 0])))
    print(dot(Vector([1, 0]), Vector([0, 0])))
    print(dot(Vector([1, 0]), Vector([1, 0])))
    print(dot(Vector([1, 0]), Vector([0, 1])))
    print(dot(Vector([1, 1]), Vector([1, 1])))
    print(dot(Vector([4, 2]), Vector([2, 1])))
