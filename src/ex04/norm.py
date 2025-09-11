from __future__ import annotations

from typing import TypeVar
from numbers import Number
import math

from vector import Vector

T = TypeVar("T", bound = Number)


def norm1(v: Vector[T]) -> float:
    """Return the Manhattan norm (sum of |vi|) of v.

    Complexity: Θ(n) time, O(1) extra space.
    """
    return float(sum(abs(x) for x in v))


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


def norm_inf(v: Vector[T]) -> float:
    """Return the supremum norm (max of vi) of v.

    Complexity: Θ(n) time, O(1) extra space.
    """
    return float(max((abs(x) for x in v), default = 0.0))