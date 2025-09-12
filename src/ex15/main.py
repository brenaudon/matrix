from complex import Complex as C
from all_previous import *

def main():
    print("=== Scalars and lerp ===", "\n")
    a, b = C(1.0, 2.0), C(-0.5, 0.25)
    print("a =", a, " b =", b)
    print("lerp(a,b,0.3) =", lerp(a, b, 0.3), "\n")

    print("\n=== Vectors ===", "\n")
    u = Vector([C(1, 1), C(-2, 0.5), C(0, -1)])
    v = Vector([C(2, -1), C(3, 4), C(1, 0)])
    print("u =", u)
    print("v =", v, "\n")
    print("linear_combination([u,v], [1+i, 0.5−i]) =",
          linear_combination([u, v], [C(1,1), C(0.5, -1)]), "\n")
    print("dot(u, v) =", dot(u, v), "\n")
    print("dot(u, u) =", dot(u, u), "\n")
    print("norm1(u) =", norm1(u), "\n", "  norm2(u) =", norm2(u), "\n", "  norm_inf(u) =", norm_inf(u), "\n")
    print("angle_cos(u, v) =", angle_cos(u, v), "\n")
    print("lerp(u, v, 0.25) =", lerp(u, v, 0.25), "\n")

    print("\n=== Cross product ===", "\n")
    a3 = Vector([C(1,1), C(0,0), C(0,0)])
    b3 = Vector([C(0,0), C(1,-1), C(0,0)])
    print("cross(a3, b3) =", cross_product(a3, b3), "\n")

    print("\n=== Matrices ===", "\n")
    A = Matrix([[C(1,0), C(2,-1)],
                [C(3,2), C(4, 0)]])
    B = Matrix([[C(0,1), C(1,0)],
                [C(2,0), C(0,-1)]])
    w = Vector([C(1,0), C(0,1)])

    print("A =", A)
    print("B =", B, "\n")
    print("A·w =", mat_vec_mul(A, w))
    print("A·B =", mat_mat_mul(A, B), "\n")
    print("trace(A) =", trace(A), "\n")
    print("transpose(A) =", transpose(A), "\n")
    print("det(A) =", determinant(A), "\n")
    invA = inverse(A)
    print("inverse(A) =", invA)
    print("A·inverse(A) =", mat_mat_mul(A, invA), "\n")

    print("\n=== Row echelon & rank ===", "\n")
    M = Matrix([
        [C(1,0), C(2,0), C(3,0)],
        [C(2,0), C(4,0), C(6,0)],
        [C(1,1), C(0,1), C(1,0)],
    ])
    print("row_echelon(M) =", row_echelon(M), "\n")
    print("rank(M) =", rank(M), "\n")

if __name__ == "__main__":
    main()
