"""
Exercise 09 – Transpose

Free‑function implementation that leaves your original `Matrix` class intact.
Time complexity : Θ(n·m) (one assignment per entry)
Space complexity: Θ(n·m) (the returned matrix)

    from ex09 import transpose
"""
from __future__ import annotations

from typing import TypeVar
from numbers import Number

from matrix import Matrix

T = TypeVar("T", bound=Number)


def transpose(mat: Matrix[T]) -> Matrix[T]:
    """Return the transpose matrix B = Aᵀ.

    Time complexity: Θ(n·m) (one assignment per entry)
    Space complexity: Θ(n·m) (the returned matrix)
    """
    rows, cols = mat.shape()

    data_t = [[mat[r, c] for r in range(rows)] for c in range(cols)]

    return Matrix(data_t)