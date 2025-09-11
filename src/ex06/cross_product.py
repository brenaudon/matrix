from __future__ import annotations

from typing import TypeVar
from numbers import Number
import math

from vector import Vector

T = TypeVar("T", bound = Number)


def cross_product(u: Vector[T], v: Vector[T]) -> Vector[T]:
    """Return the 3‑D cross product u × v.

    Time complexity: Θ(1)   (a constant 9 multiplies/adds)
    Space complexity: Θ(1)   (one new 3‑element Vector)
    """
    if len(u) != 3 or len(v) != 3:
        raise ValueError("Cross product is only defined for 3‑D vectors")

    ux, uy, uz = u[0], u[1], u[2]
    vx, vy, vz = v[0], v[1], v[2]

    fma = getattr(math, "fma", None)

    if fma is not None and all(isinstance(x, float) for x in (ux, uy, uz, vx, vy, vz)):
        cx = fma(uy, vz, -uz * vy)   # uy*vz − uz*vy
        cy = fma(uz, vx, -ux * vz)   # uz*vx − ux*vz
        cz = fma(ux, vy, -uy * vx)   # ux*vy − uy*vx
    else:
        cx = uy * vz - uz * vy
        cy = uz * vx - ux * vz
        cz = ux * vy - uy * vx

    return Vector([cx, cy, cz])