from __future__ import annotations

from typing import TypeVar
from numbers import Number

from matrix import Matrix

T = TypeVar("T", bound=Number)
_EPS = 1e-10   # pivot tolerance for float inputs


def determinant(mat: Matrix[T]) -> T:
    """Return det(mat) via Gaussian elimination with partial pivoting.

    Time complexity is O(n^3) for an n×n matrix.
    Memory complexity is O(n^2) for the matrix copy.
    """
    n_rows, n_cols = mat.shape()
    if n_rows != n_cols:
        raise ValueError("Determinant is defined only for square matrices")
    n = n_rows

    # Work on a deep copy so the caller’s matrix remains intact
    A = [row.copy() for row in (mat._m if hasattr(mat, "_m")          # type: ignore[attr-defined]
                                else [[mat[r, c] for c in range(n)] for r in range(n)])]

    det: T = 1  # multiplicative identity of generic type T
    sign = 1    # track row swaps

    for col in range(n):
        # Partial pivot: find row with largest |pivot|
        pivot_row = max(range(col, n), key=lambda r: abs(A[r][col]))
        pivot_val = A[pivot_row][col]

        # If pivot is ‘zero’, determinant is zero
        try:
            is_zero = abs(pivot_val) < _EPS
        except TypeError:  # non-float
            is_zero = pivot_val == 0
        if is_zero:
            return det * 0  # correct zero of type T

        # Row swap if needed
        if pivot_row != col:
            A[col], A[pivot_row] = A[pivot_row], A[col]
            sign *= -1

        # Eliminate entries below the pivot (no scaling of pivot row)
        for r in range(col + 1, n):
            factor = A[r][col] / pivot_val
            A[r][col] = 0  # by construction
            for c in range(col + 1, n):
                A[r][c] -= factor * A[col][c]

        det *= pivot_val  # accumulate diagonal product later multiplied by sign

    return det * sign
