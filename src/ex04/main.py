from vector import Vector
from norm import norm1, norm2, norm_inf

if __name__ == "__main__":
    u = Vector([0., 0., 0.])
    print("‖u‖₁ = ", norm1(u))  # 0.0
    print("‖u‖₂ = ", norm2(u))  # 0.0
    print("‖u‖∞ = ", norm_inf(u))  # 0.0

    print(" ")

    u = Vector([1., -2., 3.])
    print("‖u‖₁ = ", norm1(u)) # 6.0
    print("‖u‖₂ = ", norm2(u)) # 3.74165738677…
    print("‖u‖∞ = ", norm_inf(u)) # 3.0

    print(" ")

    u = Vector([-1., -2.])
    print("‖u‖₁ = ", norm1(u))  # 3.0
    print("‖u‖₂ = ", norm2(u))  # 2.236067977…
    print("‖u‖∞ = ", norm_inf(u))  # 2.0