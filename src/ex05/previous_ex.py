from __future__ import annotations

from typing import TypeVar
from numbers import Number
import math

from vector import Vector

T = TypeVar("T", bound=Number)

def dot(u: Vector[T], v: Vector[T]) -> T:
    """Return the dot product ⟨u|v⟩ of two same‑size vectors.

    Time complexity  : Θ(n)   (coordinates)
    Space complexity : Θ(1)   (single accumulator)
    """
    if len(u) != len(v):
        raise ValueError("Vector size mismatch in dot product")

    # Identity of the right numeric type
    zero: T = u[0] - u[0] if u else v[0] - v[0]

    total: T = zero
    fma = getattr(math, "fma", None)

    # Optional fused multiply‑add for floats)
    if fma is not None and all(isinstance(x, float) for x in (*u, *v)):
        for a, b in zip(u, v):
            total = fma(a, b, total)
    else:
        for a, b in zip(u, v):
            total += a * b

    return total

def norm2(v: Vector[T]) -> float:
    """Return the Euclidean norm (root of sum of squares) of v.

    Complexity: Θ(n) time, O(1) extra space.
    """
    total = 0.0
    fma = getattr(math, "fma", None)
    if fma is not None:
        for x in v:
            total = fma(x, x, total)
    else:
        for x in v:
            total += x * x
    return math.sqrt(total)