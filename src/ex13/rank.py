from __future__ import annotations

from typing import TypeVar
from numbers import Number

from matrix import Matrix
from row_echelon import row_echelon

T = TypeVar("T", bound=Number)
_EPS = 1e-10


def _is_zero_scalar(x: T) -> bool:  # type: ignore[return-value]
    """Zero‑test"""
    try:
        return abs(x) < _EPS
    except TypeError:  # non‑abs‑supporting types (e.g. Fractions)
        return x == 0


def rank(mat: Matrix[T]) -> int:
    """Return the rank of matrix.

    Time complexity: O(n^3) for an n x n matrix.
    Space complexity: O(n^2) for an n x n matrix.
    """
    ref = row_echelon(mat)
    rows, cols = ref.shape()

    def is_zero_row(r: int) -> bool:
        return all(_is_zero_scalar(ref[r, c]) for c in range(cols))

    return sum(not is_zero_row(r) for r in range(rows))