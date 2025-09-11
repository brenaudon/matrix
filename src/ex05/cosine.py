from __future__ import annotations

from typing import TypeVar
from numbers import Number

from vector import Vector
from previous_ex import dot, norm2

T = TypeVar("T", bound = Number)


def angle_cos(u: Vector[T], v: Vector[T]) -> float:
    """Return cos(u,v) = ⟨u|v⟩ / (‖u‖₂ * ‖v‖₂).

    Time complexity: Θ(n) (coordinates)
    Space complexity: Θ(1) (single accumulator)
    """
    if len(u) != len(v):
        raise ValueError("Vectors must have identical dimensions")

    num = dot(u, v) # ⟨u|v⟩
    du = norm2(u) # ‖u‖₂
    dv = norm2(v) # ‖v‖₂

    if du == 0.0 or dv == 0.0:
        raise ValueError("Cosine undefined for zero‑length vector(s)")

    return float(num) / (du * dv)
