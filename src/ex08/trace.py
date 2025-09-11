from __future__ import annotations

from typing import TypeVar
from numbers import Number

from matrix import Matrix

T = TypeVar("T", bound = Number)


def trace(mat: Matrix[T]) -> T:
    """Return trace(mat) = sum of the diagonal elements.

    Time complexity: Θ(n), where n is the number of rows (or columns).
    Space complexity: Θ(1) extra space.
    """
    if not mat.is_square():
        raise ValueError("Matrix must be square")

    # Additive identity of the correct numeric type
    acc: T = mat[0][0] - mat[0][0]

    rows, _ = mat.shape()

    for i in range(rows):
        acc += mat[i][i]

    return acc