from __future__ import annotations

from typing import TypeVar
from numbers import Number

from matrix import Matrix

T = TypeVar("T", bound=Number)
_EPS = 1e-10  # tolerance for pivoting floats


def _is_zero(x: T) -> bool:  # type: ignore[return-value]
    try:
        return abs(x) < _EPS
    except TypeError:
        return x == 0

def inverse(mat: Matrix[T]) -> Matrix[T]:
    """Return the inverse of matrix.

    Time complexity: O(n^3) where n is the number of rows/columns in the matrix.
    Space complexity: O(n^2) for the augmented matrix.
    """
    n_rows, n_cols = mat.shape()
    if n_rows != n_cols:
        raise ValueError("Inverse exists only for square matrices")
    n = n_rows

    # Build the augmented matrix [A | I]
    A = [row.copy() for row in (mat._m if hasattr(mat, "_m")          # type: ignore[attr-defined]
                                else [[mat[r, c] for c in range(n)] for r in range(n)])]
    I = [[mat[0, 0] - mat[0, 0] for _ in range(n)] for _ in range(n)]  # zero matrix of type T
    for i in range(n):
        I[i][i] = I[i][i] + 1     # set to 1 of type T
    aug = [A[i] + I[i] for i in range(n)]  # each row: A | I

    # Gauss–Jordan elimination
    pivot_row = 0
    for col in range(n):
        # pivot search
        pivot = next((r for r in range(pivot_row, n) if not _is_zero(aug[r][col])), None)
        if pivot is None:
            raise ValueError("Matrix is singular (zero pivot)")
        # swap
        if pivot != pivot_row:
            aug[pivot_row], aug[pivot] = aug[pivot], aug[pivot_row]
        # scale pivot row
        pv = aug[pivot_row][col]
        scale = [x / pv for x in aug[pivot_row]]  # type: ignore[operator]
        aug[pivot_row] = scale
        # eliminate other rows
        for r in range(n):
            if r == pivot_row:
                continue
            factor = aug[r][col]
            if _is_zero(factor):
                continue
            aug[r] = [x - factor * y for x, y in zip(aug[r], aug[pivot_row])]
        pivot_row += 1
    # Extract inverse from right half
    inv_data = [row[n:] for row in aug]
    return Matrix(inv_data)