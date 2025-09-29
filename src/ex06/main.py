from vector import Vector
from cross_product import cross_product

if __name__ == "__main__":
    pairs = [
        (Vector([0., 0., 1.]), Vector([1., 0., 0.]), Vector([0., 1., 0.])),
        (Vector([1., 2., 3.]), Vector([4., 5., 6.]), Vector([-3., 6., -3.])),
        (Vector([4., 2., -3.]), Vector([-2., -5., 16.]), Vector([17., -58., -16.])),
    ]
    for u, v, ref in pairs:
        out = cross_product(u, v)
        print(f"{u} × {v} = {out}")
        assert all(abs(o - r) < 1e-9 for o, r in zip(out, ref))

    print("\n=== Tests from correction ===\n")

    print(cross_product(Vector([0, 0, 0]), Vector([0, 0, 0])))
    print(cross_product(Vector([1, 0, 0]), Vector([0, 0, 0])))
    print(cross_product(Vector([1, 0, 0]), Vector([0, 1, 0])))
    print(cross_product(Vector([8, 7, -4]), Vector([3, 2, 1])))
    print(cross_product(Vector([1, 1, 1]), Vector([0, 0, 0])))
    print(cross_product(Vector([1, 1, 1]), Vector([1, 1, 1])))
